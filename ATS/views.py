from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *


def index(request):
    return render(request,"index.html/")

def logIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html/', {'form': form})

def signUp(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, 'Your account has been created!')
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'Your account has been created!')
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})

def signOut(request):
    logout(request)
    return redirect('/')

def index2(request):
    if request.method == 'POST':
        form =  contactus(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = contactus()
        return render(request,'contactus.html/',{'form':form})

def upload_form(request):
    if request.method == 'POST':
        form = upload1(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = upload1()
        return render(request, 'uploadpage.html/', {'form': form})

def technews(request):
    display = Upload.objects.all()
    print(display)
    params = {'Upload':display}
    return render(request,'technews.html/',params)

def job_notify(request):
    if request.method == 'POST':
        form = Jobnoti(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Jobnoti()
        return render(request, 'jobUpload.html/', {'form': form})

def job(request):
    display = Job_upload.objects.all()
    print(display)
    params = {'Job_upload':display}
    return render(request,'JobNotification.html/',params)

