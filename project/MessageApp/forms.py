from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import PrivateMessage
from django.forms import Textarea


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMessage
        fields = ('message',)