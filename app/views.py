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

def About(request):
    return render(request,'about.html')


def Contact(request):
    return render(request,'contact.html')

def profile(request):
    return render(request,'profile.html')


def User_SignUp(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            Email=fm.cleaned_data['email']
            messages.success(request,'Successfully Registered')
            send_mail(' Registration Successfull', 'Signup and Registration Was Successfull Congratulations Now You can read and Write Blogs On My Website.',
                      'priyakota44@gmail.com', [str(Email)], fail_silently=False)
            print("Form is Validated...")
            print("Email sent was SuccessFull...")
            fm.save()
            
            return HttpResponseRedirect('/home/home')
    else:
        fm=SignUpForm()
    return render(request,'signup.html',{"form":fm})


def User_Login(request):
    print(request.user)
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                un=fm.cleaned_data['username']
                up=fm.cleaned_data['password']
                user=authenticate(username=un,password=up)

                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully')

                    return HttpResponseRedirect('/home/profile')

        else:
            fm=AuthenticationForm()
        return render(request,'login.html',{"form":fm})
    else:
        return HttpResponseRedirect('/home/home')

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect('/home/home')
    return render(request,'logout.html')
