from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db.models import Q, F, aggregates
from django.http import QueryDict

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from accounts.models import User
from .models import Game, Record
from .serializers import GameSerializer, RecordSerializer

from django.views import View

import datetime, time, json
from datetime import date, timedelta

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail(request, game_pk):
    game = get_object_or_404(Game, pk=game_pk)
    serializer = GameSerializer(game)
    return Response(serializer.data)


class RecordView(APIView):
    @permission_classes([IsAuthenticated])
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
            count = int(request.GET['count'])
        except KeyError:
            print('KeyError: count 값이 존재하지 않습니다.')
        except ValueError:
            print('ValueError: count 값이 숫자가 아닙니다.')
            return Response({'ValueError': 'count값이 유효하지 않습니다.\ncount: %s' % request.GET['count']}, status=status.HTTP_400_BAD_REQUEST)
        if count > 100:
            return Response({'KeyError': 'count값이 너무 큽니다.\ncount: %s > 100' % count}, status=status.HTTP_400_BAD_REQUEST)

        # sort 요청 확인
        try:
            sort_method = request.GET['sort']
        except:
            print('KeyError: sort 값이 존재하지 않습니다.')
        if sort_method != 'high' and sort_method != 'lastest':
            return Response({'ValueError': 'sort값이 유효하지 않습니다.\nsort: %s\n"high" 또는 "lastest"로 요청하세요' % request.GET['count']}, status=status.HTTP_400_BAD_REQUEST)
        
        # week 요청 확인
        try:
            week_method = request.GET['week']
            if week_method.lower() == 'true':
                week_method = True
            elif week_method.lower() == 'false':
                week_method = False
            else:
                return Response({'ValueError': 'week값이 유효하지 않습니다.\nweek: %s\n"true" 또는 "false"로 요청하세요' % request.GET['count']}, status=status.HTTP_400_BAD_REQUEST)
        except:
            print('ValueError: week 값이 존재하지 않습니다.')
            week_method = False
            
        # 쿼리 성능이슈 존재 가능
        ####################################################
        if user_pk:
            records = Record.objects.filter(Q(game_id=game_pk) & Q(user_id=user_pk))
        else:
            records = Record.objects.filter(Q(game_id=game_pk))
        
        if week_method:
            from_monday = date.today().weekday()
            records = records.filter(start_time__gte=date.today()-timedelta(days=from_monday))

        if sort_method == 'high':
            records = records.order_by('-score')
        else:
            records = records.order_by('-start_time')
        ###################################################

        serializer = RecordSerializer(records[:count], many=True)
        return Response(serializer.data)
    
    @permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def get_rank(request, game_pk):
    try:
        week_method = request.GET['week']
        if week_method.lower() == 'true':
            week_method = True
        elif week_method.lower() == 'false':
            week_method = False
        else:
            return Response({'ValueError': 'week값이 유효하지 않습니다.\nweek: %s\n"true" 또는 "false"로 요청하세요' % request.GET['count']}, status=status.HTTP_400_BAD_REQUEST)
    except:
        print('ValueError: week 값이 존재하지 않습니다.')
        week_method = False
    
    try:
        count = int(request.GET['count'])
    except KeyError:
        print('KeyError: count 값이 존재하지 않습니다.')
        count = 100
    except ValueError:
        print('ValueError: count 값이 숫자가 아닙니다.')
        return Response({'ValueError': 'count값이 유효하지 않습니다.\ncount: %s' % request.GET['count']}, status=status.HTTP_400_BAD_REQUEST)
    if count > 100:
        return Response({'KeyError': 'count값이 너무 큽니다.\ncount: %s > 100' % count}, status=status.HTTP_400_BAD_REQUEST)
    print(week_method)
    if week_method:
        from_monday = date.today().weekday()
        ranking = Record.objects.filter(Q(game_id=game_pk) & Q(start_time__gte=date.today()-timedelta(days=from_monday))).order_by('-score').values('user_id').annotate(
            score = aggregates.Max('score')
        )[:count]
    else:
        ranking = Record.objects.filter(game_id=game_pk).order_by('-score').values('user_id').annotate(
            score = aggregates.Max('score')
        )[:count]

    for r in ranking:
        uid = r.pop('user_id')
        user = User.objects.get(id=uid)
        r['user'] = user
    serializer = RecordSerializer(ranking, many=True)
    return Response(serializer.data)