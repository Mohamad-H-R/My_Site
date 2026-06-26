from django.contrib import admin
from django.urls import path

from blog.views import *
from website.views import *
app_name = 'blog'

urlpatterns = [
    path('blog_home', blog_home_view, name='blog_home'),
    path('blog_single', blog_single_view, name='blog_single'),
]