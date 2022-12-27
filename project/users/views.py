from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, MessageForm
from .models import userMessage, adminMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'users/home.html')


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

def message(request):
    adminReply = adminMessage.objects.all()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Thanks for contacting the admin. We'll reply you soon")
        return redirect('home')
    else:
        form = MessageForm()
        mo = userMessage.objects.all()
    return render(request, 'users/message.html', {'form':MessageForm,'messageObjects':mo,'adminMessage':adminReply})
