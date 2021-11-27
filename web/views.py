from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404
from .models import *

import json


def transliterate(name):
    res = ''
    with open("web/json/translit.json", "r") as file:
        mp = json.load(file)
        for ch in name.lower():
            try:
                res += mp[ch]
            except:
                res += ch

    return res


def homepage(request):
    return render(request, 'base.html')


def student_view(request, slug):
    student = get_object_or_404(Student, slug__iexact=slug)
    return render(request, 'student_view.html', {'student': student})

def students_view(request, slug):
    student = get_object_or_404(Student, slug__iexact=slug)
    print(transliterate(student.username))
    return render(request, 'student_view.html', {'student': student})

