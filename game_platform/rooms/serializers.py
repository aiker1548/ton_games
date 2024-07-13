from rest_framework import serializers
from .models import Room
from users.serializers import UserSerializer

class RoomSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    users = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = ['id', 'creator', 'deposit', 'users']
