import logging
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from kind_app.models.satisfaction import Satisfaction
from kind_app.serializers import SatisfactionSerializer

# Get a logger instance for this view
logger = logging.getLogger('kind_app')

class SatisfactionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        logger.info(f"GET request received for satisfaction data. User: {request.user.username}, PK: {pk}")
        # If a specific entry is requested
        if pk:
            logger.debug(f"Fetching specific satisfaction entry with pk={pk}")
            entry = get_object_or_404(Satisfaction, pk=pk)

            # Check if the user is the owner of the entry or an admin
            if request.user.is_superuser or entry.user == request.user:
                serializer = SatisfactionSerializer(entry)
                logger.debug(f"Returning satisfaction data for pk={pk}")
                return Response(serializer.data)
            else:
                logger.warning(f"Permission denied: User {request.user.username} attempted to access satisfaction entry {pk}")
                return Response({"detail": "You do not have permission to view this entry."}, status=status.HTTP_403_FORBIDDEN)

        # If all entries are requested
        if request.user.is_superuser:
            # Admin can see all entries
            logger.debug("Admin user requesting all satisfaction entries")
            entries = Satisfaction.objects.all()
        else:
            # Regular users can only see their own entries
            logger.debug(f"User {request.user.username} requesting their satisfaction entries")
            entries = Satisfaction.objects.filter(user=request.user)
        
        serializer = SatisfactionSerializer(entries, many=True)
        logger.debug(f"Returning {entries.count()} satisfaction entries")
        return Response(serializer.data)

    def post(self, request):
        logger.info(f"POST request received to create satisfaction entry. User: {request.user.username}")
        # Automatically set the user to the authenticated user
        data = request.data.copy()  # Make a mutable copy of the request data
        data['user'] = request.user.id  # Set the user field to the currently authenticated user

        serializer = SatisfactionSerializer(data=data)
        if serializer.is_valid():
            entry = serializer.save(user=request.user)
            logger.info(f"Successfully created satisfaction entry with id={entry.id}")
            return Response(SatisfactionSerializer(entry).data, status=status.HTTP_201_CREATED)
        logger.warning(f"Invalid data for satisfaction creation: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        entry_id = request.data.get('id', None)
        logger.info(f"PUT request received to update satisfaction entry {entry_id}. User: {request.user.username}")
        
        try:
            entry = get_object_or_404(Satisfaction, pk=entry_id)
            
            # Check if the user is the owner of the entry or an admin
            if request.user.is_superuser or entry.user == request.user:
                serializer = SatisfactionSerializer(entry, data=request.data, partial=True)
                if serializer.is_valid():
                    entry = serializer.save(user=request.user)
                    logger.info(f"Successfully updated satisfaction entry {entry_id}")
                    return Response(SatisfactionSerializer(entry).data)
                logger.warning(f"Invalid data for satisfaction update: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                logger.warning(f"Permission denied: User {request.user.username} attempted to update satisfaction entry {entry_id}")
                return Response({"detail": "You do not have permission to update this entry."}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            logger.error(f"Error updating satisfaction entry {entry_id}: {str(e)}")
            raise

    def delete(self, request):
        ids = request.data.get('ids', None)
        logger.info(f"DELETE request received for satisfaction entries with ids={ids}. User: {request.user.username}")
        
        try:
            entries = Satisfaction.objects.filter(id__in=ids)
            entry_count = entries.count()
            logger.debug(f"Found {entry_count} entries matching the requested ids")

            # Check if the user is an admin or only owns the entries they are trying to delete
            if request.user.is_superuser:
                # Admin can delete all selected entries
                logger.info(f"Admin user deleting {entry_count} satisfaction entries")
                entries.delete()
            else:
                # Regular user can only delete their own entries
                user_entries = entries.filter(user=request.user)
                user_entry_count = user_entries.count()
                
                if user_entries.exists():
                    logger.info(f"User {request.user.username} deleting {user_entry_count} of their satisfaction entries")
                    user_entries.delete()
                else:
                    logger.warning(f"Permission denied: User {request.user.username} attempted to delete entries they don't own")
                    return Response({"detail": "You do not have permission to delete these entries."}, status=status.HTTP_403_FORBIDDEN)

            logger.info("Satisfaction entries successfully deleted")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error deleting satisfaction entries: {str(e)}")
            raise
