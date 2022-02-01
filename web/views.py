from django.shortcuts import render, redirect
from django import template
from .models import *


def homepage(request):
    return render(request, 'base.html', {'isAuth': request.user.is_authenticated})


def users_view(request):
    if request.user.is_authenticated:
        isEmployer = request.user.role == 'e'
    else:
        isEmployer = None

    print(isEmployer)

    if isEmployer:
        users = CustomUser.objects.filter(role='s')
    elif isEmployer is None:
        users = []
    else:
        users = CustomUser.objects.filter(role='e')
    return render(request, 'users_view.html', {'users': users, 'isEmployer': isEmployer})


def resumes_view(request):
    resumes = Resume.objects.all()
    return render(request, 'resumes_view.html', {'resumes': resumes})


def vacancies_view(request):
    wage_min = request.GET.get('wageMin', 20000)
    wage_max = request.GET.get('wageMax', 500000)
    vacancies = Vacancy.objects.filter(wage__gte=wage_min, wage__lte=wage_max)
    return render(request, 'vacancies_view.html', {'vacancies': vacancies, 'wage_min': wage_min, 'wage_max': wage_max})


def chats_view(request):
    chats = Chat.objects.filter(members__in=[request.user.id])
    print(chats)
    return render(request, 'chats_view.html', {'chats': chats, 'user': request.user})


def chats_create(request, companion):
    nchat = Chat(members=[request.user, companion])
    nchat.save()
    return redirect(chat_view, nchat.id)


def chat_view(request, id):
    chat = Chat.objects.filter(id=id)
    messages = chat.message_set
    return render(request, 'chat_view.html', {'chat': chat, 'messages': messages})




