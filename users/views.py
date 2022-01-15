from django.shortcuts import render

from .models import *
from .forms import *


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})
