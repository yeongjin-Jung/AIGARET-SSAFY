from django.urls import path
from . import views

app_name = 'mypages'

urlpatterns = [
    path('calendar/', views.MyPageCanlendarView.as_view(), name='calendar'),
    path('imagechange/', views.ChangeProfileImageView.as_view(), name='imagechange'),
    path('goaltimechange/', views.ChangeGoalTimeView.as_view(), name='goaltimechange'),
    path('totalgametime/', views.TotalGameTimeView.as_view(), name='totalgametime'),
    path('achievepercent/', views.AchievementPercentageView.as_view(), name='achievepercent'),
    path('monthlygametime/', views.MonthlyGameTimeView.as_view(), name='monthlygametime'),
]