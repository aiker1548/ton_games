from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer
from rest_framework.permissions import AllowAny
import random


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], url_path='create-game')
    def create_game(self, request):
        room_id = request.data.get('room_id')
        player1_id = request.data.get('player_id')
        decrypted_choices = request.data.get('choices')
        bet = request.data.get('bet')
        #todo: реализовать перевод ставки на смарт-контракт
        game = Game.objects.create(room_id=room_id, player1_id=player1_id, bet=bet, decrypted_choices=decrypted_choices)
        return Response(GameSerializer(game).data)
    

    @action(detail=True, methods=['post'], url_path='connect-game')
    def connect_game(self, request, pk=None):
        game = self.get_object()
        player2_id = request.data.get('player_id')
        encrypted_choices = request.data.get('choices')
        winner_id = random.choice([game.player1_id, game.player2_id]) 
        #todo: реализовать перевод ставки на смарт-контракт, реализовать логику игры 

        game.player2_id = player2_id
        game.encrypted_choices = encrypted_choices
        game.winner_id = winner_id

        game.save()

        return Response(GameSerializer(game).data)


