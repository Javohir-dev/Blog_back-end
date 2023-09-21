from django.shortcuts import render
from django.views import View
from blog.models import Blog
from django.urls import reverse_lazy
from django.views.generic import (
    UpdateView,
    CreateView,
    DeleteView,
    DetailView,
)


class BlogsList(View):
    def get(self, request):
        all_blogs = Blog.published.all()
        context = {
            "blogs": all_blogs,
        }

        return render(request, "blogs-list.html", context)


# class BlogDetail(View):
#     def get(self, request, pk):
#         blog = Blog.published.get(id=pk)
#         context = {
#             "blog": blog,
#         }

#         return render(request, "blog-detail.html", context)


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog-detail.html"


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ["title", "body", "image", "status"]
    template_name = "crud/blog-update.html"
    success_url = reverse_lazy("blog:blogs")


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "crud/blog-delete.html"
    success_url = reverse_lazy("blog:blogs")


class BlogCreateView(CreateView):
    model = Blog
    template_name = "crud/blog-create.html"
    fields = ["title", "body", "image", "status"]
    success_url = reverse_lazy("blog:blogs")
