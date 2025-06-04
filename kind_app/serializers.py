from django.contrib.auth.models import User
from rest_framework import serializers
from kind_app.models.achievement import Achievement
from kind_app.models.kudos import Kudos
from kind_app.models.satisfaction import Satisfaction
from kind_app.models.highlight import Highlight

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)  # Only include fields you need for response

class KudosSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Include username in the response

    class Meta:
        model = Kudos
        fields = ['id', 'user', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class AchievementSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Include username in the response

    class Meta:
        model = Achievement
        fields = ['id', 'user', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class HighlightSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Include username in the response

    class Meta:
        model = Highlight
        fields = ['id', 'user', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class SatisfactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Include username in the response

    class Meta:
        model = Satisfaction
        fields = ['id', 'user', 'satisfaction', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
