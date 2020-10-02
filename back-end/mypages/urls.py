from django.urls import path
from . import views

app_name = 'mypages'

urlpatterns = [
    path('calendar/', views.MyPageCanlendarView.as_view(), name='calendar'),
    path('imagechange/', views.ChangeProfileImageView.as_view(), name='imagechange'),
    path('goaltimechange/', views.ChangeGoalTimeView.as_view(), name='goaltimechange'),
    path('achievepercent/', views.AchievementPercentageView.as_view(), name='achievepercent'),
]