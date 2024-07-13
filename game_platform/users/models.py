from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    wallet_address = models.CharField(max_length=255, unique=True)
