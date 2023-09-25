from django.urls import path
from .views import PostListView, PostCreate

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('post_create/', PostCreate.as_view(), name='create'),
]
