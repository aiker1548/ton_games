from django.db import models
from users.models import CustomUser

class Room(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_rooms')
    deposit = models.FloatField()
    users = models.ManyToManyField(CustomUser, related_name='rooms')
