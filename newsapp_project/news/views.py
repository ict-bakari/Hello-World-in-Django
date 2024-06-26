from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name='index.html'
    context_object_name = 'all_posts_list'

class AboutPageView(ListView):
    model = Post
    template_name='about.html'



