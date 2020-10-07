from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_pk>/', views.detail, name='detail'),
    path('<int:game_pk>/records/users/<int:user_pk>/', views.RecordView.as_view(), name='user_records'),
    path('<int:game_pk>/records/', views.RecordView.as_view(), name='rank'),
    # path('description/', views.update_description)
    path('<int:game_pk>/rank/', views.get_rank),
    path('<int:game_pk>/rank/<int:user_pk>/', views.get_my_rank),
]