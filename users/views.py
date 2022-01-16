from django.shortcuts import render, redirect

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


def profile(request, id):
    user = CustomUser.objects.filter(id=id)
    return render(request, 'profile.html', {'user': user})
