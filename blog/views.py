from django.shortcuts import render
from django.views import View
from blog.models import Blog


class BlogsList(View):
    def get(self, request):
        all_blogs = Blog.published.all()
        context = {
            'blogs': all_blogs,
        }

        return render(request, 'blogs-list.html', context)

class BlogDetail(View):
    def get(self, request, id):
        blog = Blog.published.get(id=id)
        context = {
            'blog': blog,
        }

        return render(request, 'blog-detail.html', context)