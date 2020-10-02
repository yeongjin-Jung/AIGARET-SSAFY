from rest_framework import serializers
from games.models import Game

class CalendarSerializer(serializers.Serializer):
    date = serializers.DateField(required=False)
    total_time = serializers.IntegerField(required=False)
    record = serializers.ListField(required=False)


