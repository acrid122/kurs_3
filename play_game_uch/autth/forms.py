from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField(max_length=68, min_length=6, widget=forms.PasswordInput(), label='Повторите пароль')

    class Meta:
        model = User
        fields = ['login', 'password', 'password2', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')

        return password2

