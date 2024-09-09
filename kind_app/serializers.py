from rest_framework import serializers
from kind_app.models.gratitude_entry import GratitudeEntry

class GratitudeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GratitudeEntry
        fields = ['id', 'user_id', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user_id', 'created_at', 'updated_at']
