from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from kind_app.models.gratitude_entry import GratitudeEntry
from kind_app.serializers import GratitudeEntrySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

class GratitudeEntryView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """List all entries for the current user."""
        gratitude_entries = GratitudeEntry.objects.filter(user_id=request.user)
        serializer = GratitudeEntrySerializer(gratitude_entries, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """Create a new gratitude entry."""
        serializer = GratitudeEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        """Update an existing gratitude entry."""
        entry_id = request.data.get('id')
        gratitude_entry = get_object_or_404(GratitudeEntry, id=entry_id, user_id=request.user)
        serializer = GratitudeEntrySerializer(gratitude_entry, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """Delete a gratitude entry."""
        entry_id = request.data.get('id')
        gratitude_entry = get_object_or_404(GratitudeEntry, id=entry_id, user_id=request.user)
        gratitude_entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
