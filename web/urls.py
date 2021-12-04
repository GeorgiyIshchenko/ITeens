from django.urls import path, include
from .apps import WebConfig
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = WebConfig.name

urlpatterns = [
    path('', homepage, name='homepage'),
    path('students/<str:slug>', student_view, name='profile_view'),
    path('students/', students_view, name='students_view'),
    path('resumes/', resumes_view, name='resumes_view'),
    path('vacancies/', vacancies_view, name='vacancies_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
