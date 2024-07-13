from django.db import models
from users.models import User

class Room(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_rooms')
    deposit = models.FloatField()
    users = models.ManyToManyField(User, related_name='rooms')
