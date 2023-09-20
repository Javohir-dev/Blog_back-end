from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('blog.urls')),
    path('', Home.as_view(), name='home')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)