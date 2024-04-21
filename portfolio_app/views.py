from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from .forms import *

# Index view
def index(request):
    # Render index.html
    return render(request, 'portfolio_app/index.html')

# View to display all posts
def posts_page(request):
    # Fetch all posts along with related user information
    posts = Post.objects.all().select_related('user')
    context = {'posts': posts}
    return render(request, 'portfolio_app/posts_page.html', context)

# View to display details of a chosen post
def post_detail(request, pk):
    # Fetch the post with the given pk along with related user information
    post = get_object_or_404(Post.objects.select_related('user'), pk=pk)
    context = {'post': post}
    return render(request, 'portfolio_app/post_details.html', context)

# View to display all users
def user_page(request):
    # Fetch all users
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'portfolio_app/user_page.html', context)


# Forms

# View to handle creation of a new post
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('posts_page')
            else:
                # Handle the case where a non-authenticated user submits the form
                return redirect('login')  # Redirect to the login page
    else:
        form = PostForm()
    return render(request, 'portfolio_app/create_post.html', {'form': form})

# View to handle updating a post
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts_page')
    else:
        form = PostForm(instance=post)
    return render(request, 'portfolio_app/update_post.html', {'form': form})

# View to handle deleting a post
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts_page')
    return render(request, 'portfolio_app/delete_post.html', {'post': post})

# View to handle joining a post
def join_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.num_joined += 1
    post.save()
    return redirect('posts_page')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the homepage after successful login
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, 'portfolio_app/login.html', {'form': form})

def register_page(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # Specify the authentication backend
            user.save()
            login(request, user)
            messages.success(request, 'Account created successfully. You can now login.')
            return redirect('index')  # Redirect to the homepage after successful registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'portfolio_app/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')