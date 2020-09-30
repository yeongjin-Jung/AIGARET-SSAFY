from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Game, Record
from .serializers import GameSerializer

from django.views import View

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


class RecordView(View):
    @permission_classes([IsAuthenticatedOrReadOnly])
    def get(self, request, game_pk, user_pk):
        records = Record.objects.all()
        return Response()
    
    @permission_classes([IsAuthenticatedOrReadOnly])
    def post(self, request, game_pk, user_pk):
        print(request.headers)
        print(request.POST)
        # record = Record()
        # record.game_no = game_pk
        # record.user_no = user_pk
        # record.start_time = 0
        

    