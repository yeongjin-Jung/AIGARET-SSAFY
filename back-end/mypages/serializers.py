from rest_framework import serializers
from games.models import Game
from django.contrib.auth import get_user_model
from games.serializers import GameSerializer

User = get_user_model()

class CalendarSerializer(serializers.Serializer):
    date = serializers.DateField(required=False)
    total_time = serializers.IntegerField(required=False)
    record = serializers.ListField(required=False)
