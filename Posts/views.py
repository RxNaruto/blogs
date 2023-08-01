from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
def UserPostView(ListView):
    model = Post
    template_name = 'Posts/post_form.html'
    context_object_name = 'posts'
    