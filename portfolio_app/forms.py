from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location', 'num_joined']  # Fields to be displayed in the form
