from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.conf import settings


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], url_path='create-room')
    def create_room(self, request):
        user_id = request.data.get('user_id')
        default_deposit = settings.DEFAULT_DEPOSIT    
        # todo: реализация перевода депозита, обработка исключений      
        room = Room.objects.create(creator_id=user_id, deposit=default_deposit)
        room.users.add(user_id)  
        return Response(RoomSerializer(room).data)

    @action(detail=True, methods=['post'], url_path='join-room')
    def join_room(self, request, pk=None):
        room = self.get_object()
        player_id = request.data.get('user_id')
        if player_id in room.users.values_list('id', flat=True):
            return Response({'detail': 'Player in room'}, status=status.HTTP_400_BAD_REQUEST)
        room.users.add(player_id)
        room.save()
        print(room.users.values_list('id', flat=True))
        return Response(RoomSerializer(room).data)

    @action(detail=True, methods=['post'], url_path='leave-room')
    def leave_room(self, request, pk=None):
        room = self.get_object()
        player_id = request.data.get('user_id')
        if player_id not in room.users.values_list('id', flat=True):
            return Response({'detail': 'Player not in room'}, status=status.HTTP_400_BAD_REQUEST)
        room.users.remove(player_id)
        room.save()
        return Response(RoomSerializer(room).data)