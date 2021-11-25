from django.shortcuts import render, redirect
from .models import *
from rest_framework.generics import get_object_or_404


def homepage(request):
    return render(request, 'base.html')


def student_view(request, slug):
    student = get_object_or_404(Student, slug__iexact=slug)
    return render(request, 'student_view.html', {'student': student})
