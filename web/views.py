from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404
from .models import *
import account.urls

import json


def homepage(request):
    return render(request, 'base.html', {'isAuth': request.user.is_authenticated})


def student_view(request, slug):
    student = get_object_or_404(Student, slug__iexact=slug)
    chats = student.chats.all()
    print(chats)
    return render(request, 'student_view.html', {'student': student, 'chats': chats})


def students_view(request):
    students = Student.objects.all()
    return render(request, 'students_view.html', {'students': students})


def resumes_view(request):
    resumes = Resume.objects.all()
    return render(request, 'resumes_view.html', {'resumes': resumes})


def vacancies_view(request):
    wage_min = request.GET.get('wageMin', 20000)
    wage_max = request.GET.get('wageMax', 500000)
    vacancies = Vacancy.objects.filter(wage__gte=wage_min, wage__lte=wage_max)
    return render(request, 'vacancies_view.html', {'vacancies': vacancies, 'wage_min': wage_min, 'wage_max': wage_max})


