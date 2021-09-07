from django.urls import path,reverse
from user import views

app_name='user'

urlpatterns = [
    path('signup',views.user_register,name='signup'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('history',views.user_game_history,name='history'),
]
