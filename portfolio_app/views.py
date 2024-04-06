from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.http import HttpResponse
from django.views import generic
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
            form.save()
            return redirect('posts_page')
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