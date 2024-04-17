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
# Pages
path('posts/', views.posts_page, name='posts_page'),
path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
path('users/', views.user_page, name='user_page'),
# Forms
path('post/create/', views.create_post, name='create_post'),
path('post/update/<int:pk>/', views.update_post, name='update_post'),
path('post/delete/<int:pk>/', views.delete_post, name='delete_post'),
path('post/join/<int:pk>/', views.join_post, name='join_post'),
path('login/', views.user_login, name='login'),
path('logout/', views.user_logout, name='logout'),
path('create_user/', views.create_user, name='create_user'),
]
