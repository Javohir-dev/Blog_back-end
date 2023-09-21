from django.urls import path

from blog.views import (
    BlogsList,
    # BlogDetail,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)


app_name = "blog"
urlpatterns = [
    path("", BlogsList.as_view(), name="blogs"),
    path("create/", BlogCreateView.as_view(), name="create"),
    # path("detail/<int:pk>/", BlogDetail.as_view(), name="detail"),
    path("detail/<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", BlogUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", BlogDeleteView.as_view(), name="delete"),
]
