from django import forms
from .models import Student, Employer, User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class EmployerForm(forms.ModelForm):

    class Meta:
        model = Employer
        fields = '__all__'
