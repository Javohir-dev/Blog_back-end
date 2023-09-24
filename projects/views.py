from django.shortcuts import render
from .forms import PostForm, CommentForm
from django.views import View
from django.views.generic import ListView
from .models import Post, Comment
class PostListView(ListView):
    model = Post
    template_name = 'projects/postlist.html'
    context_object_name = 'posts'
