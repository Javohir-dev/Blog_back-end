from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from blog.models import Ads, Blog
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView,
    DetailView,
)
from .forms import CommentForm
from django.contrib.auth.models import AnonymousUser


class BlogsList(View):
    def get(self, request):
        all_blogs = Blog.published.all()
        ads = Ads.objects.all()
        context = {
            "blogs": all_blogs,
            "ads": ads,
        }

        return render(request, "blogs-list.html", context)


# class BlogDetail(View):
#     def get(self, request, pk):
#         blog = Blog.published.get(id=pk)
#         context = {
#             "blog": blog,
#         }

#         return render(request, "blog-detail.html", context)


class BlogDetailView(View):
    def get(self, request, pk):
        blog = Blog.published.get(id=pk)
        comments = blog.comment.all()
        form = CommentForm()
        context = {"form": form, "blog": blog, "comments": comments}
        return render(request, "blog-detail.html", context)

    def post(self, request, pk):
        blog = Blog.published.get(id=pk)
        form = CommentForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = blog
                comment.save()
                url = reverse("blog:detail", kwargs={"pk": pk})
                return redirect(url)
            else:
                return redirect("blog:detail", kwargs={"pk": pk})
        else:
            url = reverse("account:login")
            return redirect(url)


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


# class AdsView(ListView):
#     def get(self, request):
#         ads = Ads.objects.all()

#         return render(request, "blog-detail.html", {"ads": ads})
