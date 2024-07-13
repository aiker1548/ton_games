from rest_framework import serializers
from .models import Game
from users.serializers import UserSerializer

class GameSerializer(serializers.ModelSerializer):
    player1 = UserSerializer()
    player2 = UserSerializer()

    class Meta:
        model = Game
        fields = ['id', 'room', 'player1', 'player2', 'decrypted_choices', 'encrypted_choices', 'key', 'timeout', 'winner']
