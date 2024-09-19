from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from kind_app.models.mood_log import MoodLog
from kind_app.serializers import MoodLogSerializer

class MoodLogView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            entry = get_object_or_404(MoodLog, pk=pk)
            serializer = MoodLogSerializer(entry)
            return Response(serializer.data)
        
        entries = MoodLog.objects.all()
        serializer = MoodLogSerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        
        data = request.data.copy()  # Make a mutable copy of the request data
        data['user'] = request.user.id  # Set the user field to the currently authenticated user

        serializer = MoodLogSerializer(data=data)
        if serializer.is_valid():
            entry = serializer.save(user=request.user)
            return Response(MoodLogSerializer(entry).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        entry_id = request.data.get('id', None)
        entry = get_object_or_404(MoodLog, pk=entry_id)
        serializer = MoodLogSerializer(entry, data=request.data, partial=True)
        if serializer.is_valid():
            entry = serializer.save(user=request.user)
            return Response(MoodLogSerializer(entry).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        ids = request.data.get('ids', None)
        entries = MoodLog.objects.filter(id__in=ids)
        entries.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
