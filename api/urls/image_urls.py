from django.urls import path
from ..views.image_views.upload_image_view import ImageUploadView
from ..views.image_views.color_palette_view import ColorPaletteView

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='upload-image'),
    path('palette/', ColorPaletteView.as_view(), name='color_palette')
]