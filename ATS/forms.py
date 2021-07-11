from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class contactus(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','message']

class upload1(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['Name','email','Title','Description','Image']

class Jobnoti(forms.ModelForm):
    class Meta:
        model = Job_upload
        fields = ['Role', 'Title', 'Description']