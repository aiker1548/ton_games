from rest_framework import serializers
from .models import Transaction
from users.serializers import UserSerializer

class TransactionSerializer(serializers.ModelSerializer):
    receiver = UserSerializer()
    sender = UserSerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'info', 'payload', 'receiver', 'sender', 'timestamp', 'token']
