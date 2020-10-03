from rest_framework import serializers
# from accounts.serializers import UserSerializer
from .models import Game, Record
from accounts.serializers import UserSerializer

import datetime, time

class GameSerializer(serializers.ModelSerializer):
    # user = UserSerializer(required=False)
    # created_at = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S")

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ['id', ]
        # read_only_fields = ('id', 'user', 'created_at', 'updated_at')


class RecordSerializer(serializers.ModelSerializer):
    # record json 작성시 필요한 부분
    user = serializers.PrimaryKeyRelatedField(read_only=True, required=False)
    game = serializers.PrimaryKeyRelatedField(read_only=True, required=False)
    score = serializers.IntegerField(required=False)
    start_time = serializers.DateTimeField(required=False)
    play_time = serializers.IntegerField(required=False)

    # record 모델 작성시 추가로 필요한 부분
    # write_only = 모델 작성시에만 사용하겠다
    # serializer.data에도 나타나지 않는다
    gameScore = serializers.IntegerField(write_only=True)
    startTime = serializers.DateTimeField(write_only=True)
    endTime = serializers.DateTimeField(write_only=True)

    class Meta:
        model = Record
        fields = '__all__'
        # read_only_fields = ['gameScore', ]
        # write_only_fields = ['gameScore', 'startTime', ]

    def create(self, validated_data):
        score = validated_data.pop('gameScore')
        validated_data['score'] = score
        start_time = validated_data.pop('startTime')
        validated_data['start_time'] = start_time
        end_time = validated_data.pop('endTime')
        play_time = int(end_time.timestamp() - start_time.timestamp())
        validated_data['play_time'] = play_time
        ret = super().create(validated_data)
        return ret


    # get은 instanse의 어떤 field를 커스텀해서 가져오는 것임
    # instanse의 gameScore field를 score로 커스텀해서 가져오는 것
    def get_score(self, obj):
        return obj['gameScore']

    def transform_play_time(self, obj):
        return 1