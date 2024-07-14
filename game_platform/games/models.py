from django.db import models
from users.models import CustomUser
from rooms.models import Room

class Game(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    player1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='player1_games')
    player2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='player2_games', null=True)
    decrypted_choices = models.JSONField(null=True)
    encrypted_choices = models.JSONField(null=True)
    key = models.CharField(max_length=255)
    timeout = models.IntegerField(default=60)
    winner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='won_games')
    bet = models.FloatField(null=True)