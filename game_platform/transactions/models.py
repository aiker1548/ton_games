from django.db import models
from users.models import CustomUser

class Transaction(models.Model):
    amount = models.FloatField()
    info = models.CharField(max_length=255)
    payload = models.TextField()
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_transactions')
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_transactions')
    timestamp = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=255)
