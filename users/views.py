from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import *
from .forms import *


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            redirect('auth')
    return render(request, 'register.html', {'form': form})


def auth(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                request.session['pk'] = user.pk
                login(request, user)
            else:
                messages.error(request, 'Неправильный логин или пароль, повторите попытку входа')
    return render(request, 'auth.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html', )
