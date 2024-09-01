# backend/api/urls.py

from django.urls import path, include

urlpatterns = [
    path('test/', include('api.urls.test_urls')),
    path('image/', include('api.urls.image_urls')),
]