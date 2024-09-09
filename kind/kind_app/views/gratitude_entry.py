from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from kind_app.models.gratitude_entry import GratitudeEntry
from kind_app.serializers import GratitudeEntrySerializer

class GratitudeEntryView(APIView):
    def get(self, request, pk=None):
        if pk:
            entry = get_object_or_404(GratitudeEntry, pk=pk)
            serializer = GratitudeEntrySerializer(entry)
            return Response(serializer.data)
        
        entries = GratitudeEntry.objects.all()
        serializer = GratitudeEntrySerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GratitudeEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        entry = get_object_or_404(GratitudeEntry, pk=pk)
        serializer = GratitudeEntrySerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        entry = get_object_or_404(GratitudeEntry, pk=pk)
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
