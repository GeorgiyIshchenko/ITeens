from django.urls import path, include
from .views import *


urlpatterns = [
    path('', homepage, name='homepage'),
    path('users/', users_view, name='users_view'),
    path('vacancies/', vacancies_view, name='vacancies_view'),
    path('resumes/', resumes_view, name='resumes_view'),
]
