from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1', 'password2',]

class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password"]