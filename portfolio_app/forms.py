from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location', 'num_joined'] 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
