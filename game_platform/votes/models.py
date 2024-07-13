from django.db import models
from users.models import CustomUser

class VoteOption(models.Model):
    text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

class Vote(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    multiple = models.BooleanField(default=False)
    question = models.CharField(max_length=255)

class VoteOptionAssociation(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    vote_option = models.ForeignKey(VoteOption, on_delete=models.CASCADE)