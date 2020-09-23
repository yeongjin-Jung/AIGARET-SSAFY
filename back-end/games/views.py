from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Game
from .serializers import GameSerializer

@api_view(['GET'])
def detail(request, game_pk):
    game = get_object_or_404(Game, pk=game_pk)
    serializer = GameSerializer(game)
    return Response(serializer.data)
