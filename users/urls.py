from django.urls import path, include

from .views import *
from .apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('register/', register, name='register'),
    path('auth/', auth, name='auth'),
    path('profile/', profile, name='profile')
]