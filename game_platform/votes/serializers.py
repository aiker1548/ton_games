from rest_framework import serializers
from .models import Vote, VoteOption
from users.serializers import UserSerializer

class VoteOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteOption
        fields = ['id', 'text', 'votes']

class VoteSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    options = VoteOptionSerializer(many=True)

    class Meta:
        model = Vote
        fields = ['id', 'creator', 'deadline', 'multiple', 'question', 'options']
