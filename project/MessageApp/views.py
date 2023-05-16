from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import PrivateMessage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import UserRegisterForm, MessageForm
from .models import PrivateMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')

def view_messages(request):
    sent_messages = PrivateMessage.objects.filter(sender = request.user)
    # check if the user is logged in and if they are the admin
    if request.user.is_authenticated:
        received_messages = PrivateMessage.objects.filter(recipient=request.user)
        return render(request, 'users/view_messages.html', {'received_messages': received_messages, 'sent_messages':sent_messages})
    return redirect('home')
