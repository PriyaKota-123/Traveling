from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User

from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'home.html')
def profile(request):
    return render(request,'profile.html')


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            EMAIL=fm.cleaned_data['email']
            user=fm.save()
            login(request,user)
            messages.success(request, 'Account Created Successfully !!')
            send_mail(
                'sending mail',
                'preparing',
                'priyakota44@gmail.com',
                [str(EMAIL)],
                fail_silently=False,
            )
            fm = SignUpForm()
        return render(request, 'sign.html', {'form': fm})

    else:
        fm = SignUpForm()

    return render(request,'sign.html', {'form':fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/4/')
        else:
            fm = AuthenticationForm()
        return render(request ,'login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/4/')

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect('/')
    return render(request,'logout.html')
