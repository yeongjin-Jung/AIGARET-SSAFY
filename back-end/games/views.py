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
    def get(self, request, game_pk, user_pk):
        records = Record.objects.filter(Q(game_id=game_pk) & Q(user_id=user_pk))
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
