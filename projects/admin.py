from django.contrib import admin

from .models import Post, Comment


# Register your models here.

@admin.register(Post)
class PostModel(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'github']
    search_fields = ['id', 'title']


admin.site.register(Comment)
