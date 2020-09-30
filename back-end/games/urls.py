from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_pk>/', views.detail, name='detail'),
    path('<int:game_pk>/users/<int:user_pk>/records/', views.RecordView.as_view(), name='user_records'),
]