import logging
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from kind_app.models.achievement import Achievement
from kind_app.serializers import AchievementSerializer

# Get a logger instance for this view
logger = logging.getLogger('kind_app')

class AchievementView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        logger.info(f"GET request for achievement data. User: {request.user.username}, PK: {pk}")
        # If a specific entry is requested
        if pk:
            entry = get_object_or_404(Achievement, pk=pk)

            # Check if the user is the owner of the entry or an admin
            if request.user.is_superuser or entry.user == request.user:
                serializer = AchievementSerializer(entry)
                logger.debug(f"Returning achievement data for pk={pk}")
                return Response(serializer.data)
            else:
                logger.warning(f"Permission denied: User {request.user.username} attempted to access achievement {pk}")
                return Response({"detail": "You do not have permission to view this entry."}, status=status.HTTP_403_FORBIDDEN)

        # If all entries are requested
        if request.user.is_superuser:
            # Admin can see all entries
            entries = Achievement.objects.all()
            logger.debug(f"Admin user retrieving all achievements")
        else:
            # Regular users can only see their own entries
            entries = Achievement.objects.filter(user=request.user)
            logger.debug(f"User retrieving their own achievements")
        
        serializer = AchievementSerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request):
        logger.info(f"POST request to create achievement. User: {request.user.username}")
        # Automatically set the user to the authenticated user
        data = request.data.copy()  # Make a mutable copy of the request data
        data['user'] = request.user.id  # Set the user field to the currently authenticated user

        serializer = AchievementSerializer(data=data)
        if serializer.is_valid():
            entry = serializer.save(user=request.user)
            logger.info(f"Achievement created with id={entry.id}")
            return Response(AchievementSerializer(entry).data, status=status.HTTP_201_CREATED)
        logger.warning(f"Invalid achievement data: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        entry_id = request.data.get('id', None)
        logger.info(f"PUT request to update achievement {entry_id}. User: {request.user.username}")
        
        try:
            entry = get_object_or_404(Achievement, pk=entry_id)

            # Check if the user is the owner of the entry or an admin
            if request.user.is_superuser or entry.user == request.user:
                serializer = AchievementSerializer(entry, data=request.data, partial=True)
                if serializer.is_valid():
                    entry = serializer.save(user=request.user)
                    logger.info(f"Achievement {entry_id} updated successfully")
                    return Response(AchievementSerializer(entry).data)
                logger.warning(f"Invalid achievement update data: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                logger.warning(f"Permission denied: User {request.user.username} attempted to update achievement {entry_id}")
                return Response({"detail": "You do not have permission to update this entry."}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            logger.error(f"Error updating achievement {entry_id}: {str(e)}")
            raise

    def delete(self, request):
        ids = request.data.get('ids', None)
        logger.info(f"DELETE request for achievements with ids={ids}. User: {request.user.username}")
        
        try:
            entries = Achievement.objects.filter(id__in=ids)
            count = entries.count()

            # Check if the user is an admin or only owns the entries they are trying to delete
            if request.user.is_superuser:
                # Admin can delete all selected entries
                logger.info(f"Admin deleting {count} achievements")
                entries.delete()
            else:
                # Regular user can only delete their own entries
                user_entries = entries.filter(user=request.user)
                if user_entries.exists():
                    logger.info(f"User deleting {user_entries.count()} achievements")
                    user_entries.delete()
                else:
                    logger.warning(f"Permission denied: User {request.user.username} attempted to delete achievements they don't own")
                    return Response({"detail": "You do not have permission to delete these entries."}, status=status.HTTP_403_FORBIDDEN)

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error deleting achievements: {str(e)}")
            raise
