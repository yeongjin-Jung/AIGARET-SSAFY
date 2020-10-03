from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from accounts.models import User
from .models import Game, Record
from .serializers import GameSerializer, RecordSerializer

from django.views import View

import datetime, time, json

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def index(request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def detail(request, game_pk):
    game = get_object_or_404(Game, pk=game_pk)
    serializer = GameSerializer(game)
    return Response(serializer.data)


class RecordView(APIView):
    @permission_classes([IsAuthenticatedOrReadOnly])
    def get(self, request, **kwargs):
        # url확인
        # game_pk, user_pk 확인
        game_pk = kwargs['game_pk']
        try:
            user_pk = kwargs['user_pk']
        except:
            user_pk = None

        # query string 확인
        # count 확인
        count = 100
        try:
            count = int(request.GET['count']) if 0 <= int(request.GET['count']) <= 100 else 100
        except KeyError:
            print('KeyError: count 값이 존재하지 않습니다.')
        except ValueError:
            print('ValueError: count 값이 숫자가 아닙니다.')

        # sort 요청 확인
        sort_method = 'lastest'
        try:
            sort_method = request.GET['sort']
        except ValueError:
            print('KeyError: sort 값이 존재하지 않습니다.')
        
        if sort_method == 'high':
            if user_pk is None:
                records = Record.objects.filter(Q(game_id=game_pk)).order_by('-score')[:count]
            else:
                records = Record.objects.filter(Q(game_id=game_pk) & Q(user_id=user_pk)).order_by('-score')[:count]
        else:
            if user_pk is None:
                records = Record.objects.filter(Q(game_id=game_pk)).order_by('-start_time')[:count]
            else:
                records = Record.objects.filter(Q(game_id=game_pk) & Q(user_id=user_pk)).order_by('-start_time')[:count]

        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)
    
    @permission_classes([IsAuthenticatedOrReadOnly])
    def post(self, request, game_pk, user_pk, format=None):
        if not User.objects.filter(id=user_pk).exists():
            return Response({'err': '존재하지 않는 유저 입니다'})
        if not Game.objects.filter(id=game_pk).exists():
            return Response({'err': '존재하지 않는 게임 입니다'})
        serializer = RecordSerializer(data=request.data)
        user = get_object_or_404(User, pk=user_pk)
        game = get_object_or_404(Game, pk=game_pk)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, game=game)
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response({'err': '암튼 에러임'})

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def rank(request, game_pk):
    count = int(request.GET['count']) if 0 <= int(request.GET['count']) <= 100 else 100
    records = Record.objects.filter(game_id=game_pk).order_by('-score')[:count]
    serializer = RecordSerializer(records, many=True)
    return Response(serializer.data)