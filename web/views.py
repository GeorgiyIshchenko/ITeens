from django.shortcuts import render
from .models import *


def homepage(request):
    return render(request, 'base.html', {'isAuth': request.user.is_authenticated})


def users_view(request):
    users = CustomUser.objects.all()
    return render(request, 'users_view.html', {'users': users})


def resumes_view(request):
    resumes = Resume.objects.all()
    return render(request, 'resumes_view.html', {'resumes': resumes})


def vacancies_view(request):
    wage_min = request.GET.get('wageMin', 20000)
    wage_max = request.GET.get('wageMax', 500000)
    vacancies = Vacancy.objects.filter(wage__gte=wage_min, wage__lte=wage_max)
    return render(request, 'vacancies_view.html', {'vacancies': vacancies, 'wage_min': wage_min, 'wage_max': wage_max})

