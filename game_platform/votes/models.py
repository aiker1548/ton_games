from django.db import models
from users.models import User

class VoteOption(models.Model):
    text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

class Vote(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    multiple = models.BooleanField(default=False)
    question = models.CharField(max_length=255)
    options = models.ManyToManyField(VoteOption, related_name='votes')
