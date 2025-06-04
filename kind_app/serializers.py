from django.contrib.auth.models import User
from rest_framework import serializers
from kind_app.models.kind_act import KindAct
from kind_app.models.kudos import Kudos
from kind_app.models.satisfaction import Satisfaction

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

class KindActSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Include username in the response

    class Meta:
        model = KindAct
        fields = ['id', 'user', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class SatisfactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Include username in the response

    class Meta:
        model = Satisfaction
        fields = ['id', 'user', 'satisfaction', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
