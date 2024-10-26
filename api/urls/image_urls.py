from django.urls import path
from ..views.image_views.upload_image_view import ImageUploadView
from ..views.image_views.color_palette_view import ColorPaletteView
from ..views.image_views.color_swap_view import ColorSwapView
from ..views.image_views.reset_image_view import ResetImageView
from ..views.image_views.resize_pixels_view import ResizePixelsView

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='upload-image'),
    path('palette/', ColorPaletteView.as_view(), name='color_palette'),
    path('swapColors/', ColorSwapView.as_view(), name='color_swap'),
    path('reset/', ResetImageView.as_view(), name='reset_image'),
    path('resize/' , ResizePixelsView.as_view(), name='resize_image'),
]