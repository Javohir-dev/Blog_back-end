from django.shortcuts import render
from .forms import PostForm, CommentForm
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'projects/postlist.html'
    context_object_name = 'posts'


class PostCreate(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'projects/post_create.html'
    fields = ['title', 'body', 'image', 'github', 'domain']
    success_url = reverse_lazy("posts")
