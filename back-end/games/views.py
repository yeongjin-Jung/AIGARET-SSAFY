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

        # distinct 요청 확인
        try:
            if request.GET['distinct'].lower() == 'true':
                distinct = True
            elif request.GET['distinct'].lower() == 'false':
                distinct = False
            else:
                return Response({'ValueError': 'distinct값이 유효하지 않습니다.\ndistinct: %s\n"true" 또는 "false"로 요청하세요' % request.GET['distinct']}, status=status.HTTP_400_BAD_REQUEST)
        except:
            print('ValueError: distinct 값이 존재하지 않습니다.')
            distinct = False
        
        # 쿼리 성능이슈 존재 가능
        ####################################################
        if distinct:
            if week_method:
                records = Record.objects.raw(
                    '''
                    SELECT a.* FROM games_record as a
                    INNER JOIN (
                        SELECT user_id as id, max(score) as score FROM games_record
                        WHERE game_id = %s
                        GROUP BY user_id
                    ) as b
                    ON a.user_id=b.id AND a.score = b.score
                    WHERE date(a.start_time) >= date(curdate()) - weekday(curdate())
                    ORDER BY score DESC
                    ''' % game_pk
                    )
            else:
                records = Record.objects.raw(
                    '''
                    SELECT a.* FROM games_record as a
                    INNER JOIN (
                        SELECT user_id as id, max(score) as score FROM games_record
                        WHERE game_id = %s
                        GROUP BY user_id
                    ) as b
                    ON a.user_id=b.id AND a.score = b.score
                    ORDER BY score DESC
                    ''' % game_pk
                    )
        else:
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

    if week_method:
        ranking = Record.objects.filter(game_id=game_pk).order_by('-score').values('user_id').annotate(
            score = aggregates.Max('score')
        )[:count]
    else:
        from_monday = date.today().weekday()
        ranking = Record.objects.filter(Q(game_id=game_pk) & Q(start_time__gte=date.today()-timedelta(days=from_monday))).order_by('-score').values('user_id').annotate(
            score = aggregates.Max('score')
        )[:count]

    for r in ranking:
        uid = r.pop('user_id')
        user = User.objects.get(id=uid)
        r['user'] = user
    serializer = RecordSerializer(ranking, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_description(request):
    something = [
        {
            'id': 1,
            'game_name': '쥐를 잡자',
            'game_description': '''[게임 설명]

 플레이어는 고양이가 되어 화면 상에 무작위로 등장하는 생쥐를 잡아야합니다. 점점 더 빨리 도망치는 생쥐를 잡아 최고점수에 도전해 보세요!

[주의사항]

 컴퓨터 화면으로부터 최소 1미터 이상의 간격을 유지하고 자리에서 일어나서 플레이하는 것을 권장합니다.

[재활 효과]

 상지의 불규칙적인 움직임을 지속적으로 유도하여 수술 및 질환으로 인해 감소한 ROM(Range of Motion)과 근지구력의 정상범위 회복을 기대할 수 있습니다.
 신체의 움직임을 화면 상에서 실시간으로 확인하여 고유수용성 감각에 대한 시각적 되먹임 훈련효과를 기대할 수 있습니다.
 생쥐와 손목부위의 지속적인 추적을 통해 인지 기능의 향상을 기대할 수 있습니다.

[적응증]

 근골격계 질환: 회전근개 파열, 골절, 유착성 관절낭염(오십견), 어깨관절 탈구 등 근골격계 질환으로 상지 ROM 및 근지구력에 저하를 겪은 환자
 신경계 질환: 뇌졸중, 파킨슨병, 진행성 근이영양증, 치매, 뇌성마비, 발달장애, 외상 및 질환으로 인한 신경 손상 등 뇌신경계질환으로 상지 ROM, 근지구력 및 인지능력에 저하를 겪은 환자''',
 "game_video": "https://youtu.be/v32NjYn5pSc"
        },
        {
            'id': 2,
            'game_name': '스네이크 게임',
            'game_description': '''[게임 설명]

 플레이어는  배고픈 뱀을 위해 화면 상에 무작위로 등장하는 먹이를 먹을 수 있도록 도와줘야합니다. 배고픈 뱀이 점점 더 빨리 사라지는 먹이를 놓치지 않고 무사히 먹을 수 있도록 도와주세요!

[주의사항]

 컴퓨터 화면으로부터 최소 50센치 이상의 간격을 유지하고 자리에서 앉아서 플레이하는 것을 권장합니다.

[재활 효과]

 몸통 및 머리의 굽힘, 폄 동작과 좌우 기울임 동작을 유도하여 수술 및 질환으로 인해 감소한 근지구력의 정상범위 회복과 스트레칭 효과를 기대할 수 있습니다.
  불규칙적인 기울임 동작을 유도함으로써 앉은 자세(혹은 선 자세)의 Static, Dynamic balance 향상을 기대할 수 있습니다.
 뱀과 먹이의 지속적인 추적을 통해 인지 기능의 향상을 기대할 수 있습니다.

[적응증]

 근골격계 질환: 경추, 흉추, 요추의 추간판 탈출증, LBP등 근골격계 질환으로 몸통 및 머리의 움직임 기능이 저하된 환자
 신경계 질환: 뇌졸중, 파킨슨병, 진행성 근이영양증, 치매, 뇌성마비, 발달장애, 외상 및 질환으로 인한 신경 손상 등 뇌신경계질환으로 몸통 및 머리의 Stability, Balance, 근지구력 및 인지능력에 저하를 겪은 환자''',
 "game_video": "https://youtu.be/v32NjYn5pSc"
        },
        {
            'id': 3,
            'game_name': '환상의 점프',
            'game_description': '''[게임 설명]

 플레이어는  갈길이 바쁜 여우를 위해 화면 상에 무작위로 등장하는 장애물을 피할 수 있도록 도와줘야합니다. 점점 더 빨리 달리는 여우가 넘어지지 않도록 도와주세요!

[주의사항]

 컴퓨터 화면으로부터 최소 50센치 이상의 간격을 유지하여 플레이하는 것을 권장합니다.
 이 게임은 여우가 점프를 하도록 하는 자세와 달릴 수 있도록 하는 자세를 정해야합니다. 각 행동에 맞는 버튼을 누르고 빨간 글씨가 사라질때까지 자세를 충분히 유지해 주세요. 설정을 완료한 이후 학습하기 버튼을 누르고 빨간 글씨가 사라질때까지 잠시만 기다려주세요.학습이 완료된 이후 게임시작버튼을 눌러 플레이 하면 됩니다.

[재활 효과]

 환자의 상태에 맞춰 원하는 부위의 훈련을 스스로 실행할 수 있습니다.
 여우와과 장애물의 지속적인 추적과 회피 훈련을 통해 인지 기능의 향상 및 순발력 향상을 기대할 수 있습니다.

[적응증]

 전문가의 조언에 맞게 훈련 상황을 셋팅하여 다양한 질환에 적용이 가능합니다.''',
 "game_video": "https://youtu.be/v32NjYn5pSc"
        }
    ]
    games = Game.objects.all()
    for game in games:
        for s in something:
            if s['id'] == game.id:
                data = QueryDict('', mutable=True)
                data.update(s)
                break
        print(data)
        serializer = GameSerializer(instance=game, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    games = Game.objects.all()
    return GameSerializer(games, many=True).data
    