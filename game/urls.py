from django.urls import path
from game import views

app_name='game'

urlpatterns = [
    path('topics',views.topics_page,name='topics'),
    path('play/<int:id>/<str:difficulty>',views.play_quiz,name='play'),
    path('end',views.end_game,name='end'),
]
