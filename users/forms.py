from django import forms
from django.core.exceptions import ValidationError

from .models import *


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


class AuthForm(forms.Form):
    email = forms.EmailField(max_length=36, label="Email")
    password = forms.CharField(max_length=36, widget=forms.PasswordInput(), label="Пароль")
