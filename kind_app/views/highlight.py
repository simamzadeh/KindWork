import logging
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from kind_app.models.highlight import Highlight
from kind_app.serializers import HighlightSerializer

logger = logging.getLogger('kind_app')

class HighlightView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        logger.info(f"GET highlight request. User: {request.user.username}, PK: {pk}")
        # If a specific entry is requested
        if pk:
            entry = get_object_or_404(Highlight, pk=pk)

            # Check if the user is the owner of the entry or an admin
            if request.user.is_superuser or entry.user == request.user:
                serializer = HighlightSerializer(entry)
                return Response(serializer.data)
            else:
                logger.warning(f"Permission denied: User {request.user.username} tried to access highlight {pk}")
                return Response({"detail": "You do not have permission to view this entry."}, status=status.HTTP_403_FORBIDDEN)

        # If all entries are requested
        if request.user.is_superuser:
            # Admin can see all entries
            entries = Highlight.objects.all()
        else:
            # Regular users can only see their own entries
            entries = Highlight.objects.filter(user=request.user)
        
        serializer = HighlightSerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request):
        logger.info(f"POST highlight request. User: {request.user.username}")
        # Automatically set the user to the authenticated user
        data = request.data.copy()  # Make a mutable copy of the request data
        data['user'] = request.user.id  # Set the user field to the currently authenticated user

        serializer = HighlightSerializer(data=data)
        if serializer.is_valid():
            entry = serializer.save(user=request.user)
            logger.info(f"Highlight created with id={entry.id}")
            return Response(HighlightSerializer(entry).data, status=status.HTTP_201_CREATED)
        logger.warning(f"Invalid highlight data: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        entry_id = request.data.get('id', None)
        logger.info(f"PUT highlight request for id={entry_id}. User: {request.user.username}")
        
        try:
            entry = get_object_or_404(Highlight, pk=entry_id)

            # Check if the user is the owner of the entry or an admin
            if request.user.is_superuser or entry.user == request.user:
                serializer = HighlightSerializer(entry, data=request.data, partial=True)
                if serializer.is_valid():
                    entry = serializer.save(user=request.user)
                    logger.info(f"Highlight {entry_id} updated")
                    return Response(HighlightSerializer(entry).data)
                logger.warning(f"Invalid highlight update data: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                logger.warning(f"Permission denied: User {request.user.username} tried to update highlight {entry_id}")
                return Response({"detail": "You do not have permission to update this entry."}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            logger.error(f"Error updating highlight {entry_id}: {str(e)}")
            raise

    def delete(self, request):
        ids = request.data.get('ids', None)
        logger.info(f"DELETE highlight request for ids={ids}. User: {request.user.username}")
        
        try:
            entries = Highlight.objects.filter(id__in=ids)

            # Check if the user is an admin or only owns the entries they are trying to delete
            if request.user.is_superuser:
                # Admin can delete all selected entries
                entries.delete()
                logger.info(f"Admin deleted highlights with ids={ids}")
            else:
                # Regular user can only delete their own entries
                entries = entries.filter(user=request.user)
                if entries.exists():
                    entries.delete()
                    logger.info(f"User deleted their highlights")
                else:
                    logger.warning(f"Permission denied: User {request.user.username} tried to delete highlights they don't own")
                    return Response({"detail": "You do not have permission to delete these entries."}, status=status.HTTP_403_FORBIDDEN)

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error deleting highlights: {str(e)}")
            raise
