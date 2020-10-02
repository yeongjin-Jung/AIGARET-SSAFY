from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from games.models import Record, Game
from accounts.models import User
from .serializers import CalendarSerializer
from games.serializers import RecordSerializer
from django.db.models import Sum
from django.http.response import JsonResponse
from rest_framework import status

# Create your views here.
class MyPageCanlendarView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        game_count = Game.objects.count()
        today = request.data.get('date')
        year, month, day = tuple(today.split('-'))
        # print(year, month, day)
        user_id = self.request.user.pk
        # print(username)

        data = {"records":[]}

        for d in range(1, int(day)+1):
            day_str = str(d).zfill(2)
            
            date = year + '-' + month + '-' + day_str

            records = Record.objects.filter(start_time__year=year, start_time__month=month, start_time__day=day_str, user_id=user_id)
           
            game_record = [{"game":"","score":0, "time":0} for _ in range(game_count)]

            for record in records:
                # print("pk", record.game_id)
                # print(Game.objects.filter(pk=record.game_id).first().game_name)
                if game_record[record.game_id - 1]["game"] == "":
                    game_record[record.game_id - 1]["game"] = Game.objects.filter(pk=record.game_id).first().game_name
                game_record[record.game_id - 1]["score"] += record.score
                game_record[record.game_id - 1]["time"] += record.play_time
            
            total_time = 0
            for r in game_record:
                total_time += r["time"]

            data["records"] += [{'date':date, 'totaltime':total_time, 'record':game_record}]

        # print(data)
        return JsonResponse(data, safe=False)

class ChangeProfileImageView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        if not User.objects.filter(pk=self.request.user.pk).exists():
            return Response({"status":"fail", "message":"존재하지 않는 회원입니다."})
        user = self.request.user
        user.profile_image = request.data.get('profile_image')
        user.save()

        return Response({"status":"success"})

class ChangeGoalTimeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        if not User.objects.filter(pk=self.request.user.pk).exists():
            return Response({"status":"fail", "message":"존재하지 않는 회원입니다."})
        user = self.request.user
        user.goal_time = request.data.get('goal_time')
        user.save()

        return Response({"status":"success"})
