from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
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
            redirect('users:auth')
    return render(request, 'register.html', {'form': form})


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(max_length=36, widget=forms.PasswordInput(), label="Пароль")
    password2 = forms.CharField(max_length=36, widget=forms.PasswordInput(), label='Повторите пароль')

    class Meta:
        model = CustomUser
        fields = 'first_name', 'last_name', 'email', 'profile_pic', 'city', 'phone_number', 'role'

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise ValidationError('Пароли не совпадают')
        return self.cleaned_data['password1']


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
                redirect('users:profile')
            else:
                messages.error(request, 'Неправильный логин или пароль, повторите попытку входа')
    return render(request, 'auth.html', {'form': form})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('users:auth')
    return render(request, 'logout.html')


@login_required
def profile(request, id):
    user = CustomUser.objects.filter(id=id)
    return render(request, 'profile.html', {'user': user})
