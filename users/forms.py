from django import forms
from django.core.exceptions import ValidationError

from .models import *


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(max_length=36, widget=forms.PasswordInput(attrs={'label': 'Пароль'}))
    password2 = forms.CharField(max_length=36, widget=forms.PasswordInput(attrs={'label': 'Повторите пароль'}))

    class Meta:
        model = CustomUser
        fields = '__all__'

