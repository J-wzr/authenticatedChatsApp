from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, MessageForm
from .models import PrivateMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def home(request):
    return render(request, 'users/index.html' )

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
    user = request.user
    if user.is_superuser:
        messages = PrivateMessage.objects.all()
    else:
        messages = PrivateMessage.objects.filter(Q(sender=user) | Q(recipient=user)).order_by('-time')[0:2]
    if request.method == "POST":
        mform = MessageForm(request.POST)
        if mform.is_valid():
            instance = mform.save(commit=False)
            instance.sender = request.user
            instance.save()
            
        else:
            messages.MessageFailure(request, "Oops!.. sth went wrong. Try send again")
    else:
        mform = MessageForm() 
        mform.fields['recipient'].queryset = User.objects.exclude(username=user.username)
    return render(request, 'users/view_messages.html', {"messages": messages,"mform":mform,})


