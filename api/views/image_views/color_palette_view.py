from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.scripts.image_processing import get_palette_and_closest_colors
from api.models.palette_model import palettes_to_json
from api.scripts.utility.image_processing_utility import compressed_original_image_path

class ColorPaletteView(APIView):
    def get(self, request):

        palette, color_palette = get_palette_and_closest_colors(compressed_original_image_path)

        if color_palette == None or palette == None:
            return Response({"message": "Color palette could not be created"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({
                "color_palette": palette,
                "color_palette_details": palettes_to_json(color_palette)
            }, status=status.HTTP_200_OK)