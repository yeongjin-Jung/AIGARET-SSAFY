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
from datetime import datetime
from django.utils import timezone

# Create your views here.
class MyPageCanlendarView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        game_count = Game.objects.count()
        today = request.data.get('date')
        if not today:
            return(Response({"status":"fail", "message":"날짜 데이터가 없습니다."}))
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

class TotalGameTimeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        game_count = Game.objects.count()
        total_time_dict = {}
        for game_pk in range(1, game_count+1):
            game_name = Game.objects.get(id=game_pk).game_name
            total_time = Record.objects.filter(user_id=self.request.user.pk, game_id=game_pk).aggregate(Sum('play_time'))
            if not total_time["play_time__sum"]:
                total_time["play_time__sum"] = 0
            
            total_time_dict[game_name] = total_time

        return JsonResponse(total_time_dict)
        
class AchievementPercentageView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        user_id = self.request.user.pk
        start_date = timezone.make_aware(datetime.strptime(request.data.get('start_date')+' 00:00:00.000000', '%Y-%m-%d %H:%M:%S.%f'))
        end_date = timezone.make_aware(datetime.strptime(request.data.get('end_date')+' 00:00:00.000000', '%Y-%m-%d %H:%M:%S.%f'))

        # print(start_date, end_date)

        total_time_dict = Record.objects.filter(start_time__lte=end_date, start_time__gte=start_date, user_id=user_id).aggregate(Sum('play_time'))

        # obj = Record.objects.filter(start_time__lte=end_date, start_time__gte=start_date, user_id=user_id)

        # for o in obj:
        #     print(o.start_time, o.play_time)

        total_time = total_time_dict['play_time__sum']

        if not total_time:
            total_time = 0

        return Response({"total_time":total_time})

class MonthlyGameTimeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        game_count = Game.objects.count()
        user_id = self.request.user.pk
        today = request.data.get('today')
        if not today:
            return(Response({"status":"fail", "message":"날짜 데이터가 없습니다."}))
        if len(today.split('-')) != 3 or len(today) != 10:
            return(Response({"status":"fail", "message":"날짜 데이터의 형식을 yyyy-mm-dd로 입력해주세요."}))

        year, month, day = tuple(today.split('-'))
        
        user_id = self.request.user.pk
        # print(username)

        data = {"records":[]}

        year = int(year)
        month = int(month)
        if month != 12:
            last_year = year - 1
            for m in range(month+1, 13):
                year_month = str(last_year) + '-' + str(m).zfill(2)
                game_record = []
                for game_pk in range(1, game_count+1):
                    game_name = Game.objects.get(id=game_pk).game_name
                    total_time = Record.objects.filter(user_id=self.request.user.pk, game_id=game_pk, start_time__year=last_year, start_time__month=m).aggregate(Sum('play_time'))
                    time = total_time["play_time__sum"] if total_time["play_time__sum"] else 0
                    game_record.append({"game":game_name, "time":time})
                monthly_record = {"date":year_month, "record":game_record}
                data["records"].append(monthly_record)
        for m in range(1, month+1):
            year_month = str(year) + '-' + str(m).zfill(2)
            game_record = []
            for game_pk in range(1, game_count+1):
                game_name = Game.objects.get(id=game_pk).game_name
                total_time = Record.objects.filter(user_id=self.request.user.pk, game_id=game_pk, start_time__year=year, start_time__month=m).aggregate(Sum('play_time'))
                time = total_time["play_time__sum"] if total_time["play_time__sum"] else 0
                game_record.append({"game":game_name, "time":time})
            monthly_record = {"date":year_month, "record":game_record}
            data["records"].append(monthly_record)
        # print(data)
        return JsonResponse(data, safe=False)