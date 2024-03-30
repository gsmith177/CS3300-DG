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
