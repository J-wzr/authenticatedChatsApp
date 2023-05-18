from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import PrivateMessage
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MessageForm(ModelForm):
    class Meta:
        model = PrivateMessage
        fields = ['sender','recipient','message']
        # exclude = ('time',)
