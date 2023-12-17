from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class StatForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['user_id', 'amount_all', 'amount_true', 'amount_false']

