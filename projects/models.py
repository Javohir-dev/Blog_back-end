from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='projects/post_images/', default='projects/default.png')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    github = models.URLField(max_length=150)
    domain = models.URLField(max_length=50)
    ordering = ['-created_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    author = models.CharField(max_length=50, verbose_name='Ism kiriting: ')
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
