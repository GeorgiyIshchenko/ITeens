from django import forms
from django.core.exceptions import ValidationError

from .models import *


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(max_length=36, widget=forms.PasswordInput(), label="Пароль")
    password2 = forms.CharField(max_length=36, widget=forms.PasswordInput(), label='Повторите пароль')

    class Meta:
        model = CustomUser
        fields = 'first_name', 'last_name', 'email', 'profile_pic', 'city', 'phone_number', 'role'
