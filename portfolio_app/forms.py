from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location', 'num_joined']  # Fields to be displayed in the form

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    skill_level = forms.ChoiceField(choices=User.SKILL_LEVEL)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['name', 'email', 'skill_level']