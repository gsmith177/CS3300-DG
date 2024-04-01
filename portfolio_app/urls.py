from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('', views.index, name='login'),
path('admin/', admin.site.urls),
path('post/<int:pk>/', views.PostsView.as_view(), name='PostsView'),
path('portfolio/<int:pk>/', views.PortfolioDetailView.as_view(), name='PortfolioDetailView'),
]
