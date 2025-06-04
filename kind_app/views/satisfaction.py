from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from kind_app.models.satisfaction import Satisfaction
from kind_app.serializers import SatisfactionSerializer

class SatisfactionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        # If a specific entry is requested
        if pk:
            entry = get_object_or_404(Satisfaction, pk=pk)

            # Check if the user is the owner of the entry or an admin
            if request.user.is_superuser or entry.user == request.user:
                serializer = SatisfactionSerializer(entry)
                return Response(serializer.data)
            else:
                return Response({"detail": "You do not have permission to view this entry."}, status=status.HTTP_403_FORBIDDEN)

        # If all entries are requested
        if request.user.is_superuser:
            # Admin can see all entries
            entries = Satisfaction.objects.all()
        else:
            # Regular users can only see their own entries
            entries = Satisfaction.objects.filter(user=request.user)
        
        serializer = SatisfactionSerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Automatically set the user to the authenticated user
        data = request.data.copy()  # Make a mutable copy of the request data
        data['user'] = request.user.id  # Set the user field to the currently authenticated user

        serializer = SatisfactionSerializer(data=data)
        if serializer.is_valid():
            entry = serializer.save(user=request.user)
            return Response(SatisfactionSerializer(entry).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        entry_id = request.data.get('id', None)
        entry = get_object_or_404(Satisfaction, pk=entry_id)

        # Check if the user is the owner of the entry or an admin
        if request.user.is_superuser or entry.user == request.user:
            serializer = SatisfactionSerializer(entry, data=request.data, partial=True)
            if serializer.is_valid():
                entry = serializer.save(user=request.user)
                return Response(SatisfactionSerializer(entry).data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "You do not have permission to update this entry."}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request):
        ids = request.data.get('ids', None)
        entries = Satisfaction.objects.filter(id__in=ids)

        # Check if the user is an admin or only owns the entries they are trying to delete
        if request.user.is_superuser:
            # Admin can delete all selected entries
            entries.delete()
        else:
            # Regular user can only delete their own entries
            entries = entries.filter(user=request.user)
            if entries.exists():
                entries.delete()
            else:
                return Response({"detail": "You do not have permission to delete these entries."}, status=status.HTTP_403_FORBIDDEN)

        return Response(status=status.HTTP_204_NO_CONTENT)
