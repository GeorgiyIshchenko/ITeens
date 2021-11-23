from django.urls import path, include
from .apps import WebConfig
from .views import *

app_name = WebConfig.name

urlpatterns = [
    path('', homepage, name='homepage'),
]
