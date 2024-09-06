from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.scripts.image_processing import get_color_palette_from_original_image

class ColorPaletteView(APIView):
    def get(self, request):

        color_palette = get_color_palette_from_original_image()

        if color_palette == None:
            return Response({"message": "Color palette could not be created"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(color_palette, status=status.HTTP_200_OK)