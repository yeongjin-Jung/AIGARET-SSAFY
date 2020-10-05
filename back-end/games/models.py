from django.db import models
from django.conf import settings
from accounts.models import User

class Game(models.Model):
    game_name = models.CharField(max_length=70, blank=False)
    game_description = models.TextField()
    game_video = models.CharField(max_length=100)

# class Report(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_report')
#     game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_report')
#     total_play_time = models.DateTimeField()

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_record')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_record')
    score = models.IntegerField()
    start_time = models.DateTimeField()
    play_time = models.IntegerField()