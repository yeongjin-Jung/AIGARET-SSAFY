from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('<int:game_pk>/', views.detail, name='detail'),
]