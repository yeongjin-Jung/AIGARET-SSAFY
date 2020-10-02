from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    path('calendar/', views.MyPageCanlendarView.as_view(), name='calendar'),
]