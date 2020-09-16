from django.db import models
from django.conf import settings
from accounts.models import User

class Game(models.Model):
    game_name = models.CharField(max_length=70, blank=False)
    game_description = models.TextField()
    game_video = models.CharField(max_length=100)

class Report(models.Model):
    user_no = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_report')
    total_play_time = models.TimeField()

class Record(models.Model):
    user_no = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_record')
    game_no = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_record')
    score = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    play_time = models.TimeField()