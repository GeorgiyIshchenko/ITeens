from django.urls import path, include

from .views import *
from .apps import WebConfig

app_name = WebConfig.name


urlpatterns = [
    path('', homepage, name='homepage'),
    path('users/', users_view, name='users_view'),
    path('vacancies/', vacancies_view, name='vacancies_view'),
    path('resumes/', resumes_view, name='resumes_view'),
    path('chats/', chats_view, name='chats_view'),
    path('chats/create', chats_create, name='chat_create'),
    path('chats/<str:chat_id>', chat_view, name='chat_view'),
]
