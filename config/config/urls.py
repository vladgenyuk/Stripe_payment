from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('core/', include('apps.core.urls'))
]

urlpatterns += doc_urls
