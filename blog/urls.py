from django.urls import path

from blog.views import BlogsList, BlogDetail


app_name = "blog"
urlpatterns = [
    path('', BlogsList.as_view(), name='blogs'),
    path('detail/<int:id>/', BlogDetail.as_view(), name='detail'),
]
