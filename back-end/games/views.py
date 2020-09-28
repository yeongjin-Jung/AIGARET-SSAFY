from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Game
from .serializers import GameSerializer

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
