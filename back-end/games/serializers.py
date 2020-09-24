from rest_framework import serializers
# from accounts.serializers import UserSerializer
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    # user = UserSerializer(required=False)
    # created_at = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S")

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ['id', ]
        # read_only_fields = ('id', 'user', 'created_at', 'updated_at')