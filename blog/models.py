from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Blog.Status.Published)


class Blog(models.Model):
    """Blog class"""

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=250)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    image = models.ImageField(upload_to="blog/images")
    published_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.Draft
    )

    objects = models.Manager()  # defauld manager
    published = PublishedManager()

    class Meta:
        ordering = ["-published_time"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comment")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username


class Ads(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
