from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.http import HttpResponse
from django.views import generic
from .models import *
# from .forms import *
# Create your views here.
def index(request):
# Render index.html
    return render( request, 'portfolio_app/index.html')

class PostsView(DetailView):
    model = Post
    template_name = 'portfolio_app/posts_page.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['user'] = post.project_set.all()
        return context

def post_detail(request, pk):
    project = get_object_or_404(Post, pk=pk)
    return render(request, 'portfolio_app/post_page.html', {'Post': Post})