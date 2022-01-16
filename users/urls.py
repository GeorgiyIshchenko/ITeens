from django.urls import path, include

from .views import *
from .apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('register/', register, name='register'),
    path('auth/', auth, name='auth'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/<str:id>', profile, name='profile'),
]
