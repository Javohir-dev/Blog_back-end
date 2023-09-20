from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "published_time", "status"]
    list_filter = ["status", "created_time", "published_time"]
    search_fields = ["title", "body"]
    ordering = ["status", "published_time"]