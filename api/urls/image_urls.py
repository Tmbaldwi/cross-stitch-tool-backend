from django.urls import path
from ..views.image_view import ImageUploadView

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='upload-image')
]