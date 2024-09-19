from django.contrib.auth.models import User
from rest_framework import serializers
from kind_app.models.gratitude_entry import GratitudeEntry
from kind_app.models.kind_act import KindAct
from kind_app.models.mood_log import MoodLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)  # Only include fields you need for response

class GratitudeEntrySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Include username in the response

    class Meta:
        model = GratitudeEntry
        fields = ['id', 'user', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class KindActSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Include username in the response

    class Meta:
        model = KindAct
        fields = ['id', 'user', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class MoodLogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Include username in the response

    class Meta:
        model = MoodLog
        fields = ['id', 'user', 'mood', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
