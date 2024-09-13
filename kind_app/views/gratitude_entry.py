from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from kind_app.models.gratitude_entry import GratitudeEntry
from kind_app.serializers import GratitudeEntrySerializer

class GratitudeEntryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            entry = get_object_or_404(GratitudeEntry, pk=pk)
            serializer = GratitudeEntrySerializer(entry)
            return Response(serializer.data)
        
        entries = GratitudeEntry.objects.all()
        serializer = GratitudeEntrySerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        
        data = request.data.copy()  # Make a mutable copy of the request data
        data['user'] = request.user.id  # Set the user field to the currently authenticated user

        serializer = GratitudeEntrySerializer(data=data)
        if serializer.is_valid():
            entry = serializer.save(user=request.user)
            return Response(GratitudeEntrySerializer(entry).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        entry_id = request.data.get('id', None)
        entry = get_object_or_404(GratitudeEntry, pk=entry_id)
        serializer = GratitudeEntrySerializer(entry, data=request.data, partial=True)
        if serializer.is_valid():
            entry = serializer.save(user=request.user)
            return Response(GratitudeEntrySerializer(entry).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        ids = request.data.get('ids', None)
        entries = GratitudeEntry.objects.filter(id__in=ids)
        entries.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
