import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse
from api.scripts.swap_image_color import swap_image_color
from api.scripts.utility.image_processing_utility import image_path_valid

current_dir = os.path.dirname(os.path.abspath(__file__))

mod_image_path = os.path.join(current_dir, '..', '..', '..', 'media', 'modified_image.png')

class ColorSwapView(APIView):
    def post(self, request):
        original_color = request.data.get("originalColor")
        print(original_color)
        new_color = request.data.get("newColor")

        swap_color_worked = swap_image_color(original_color, new_color)

        if not swap_color_worked:
            return Response({"message": "Colors could not be swapped"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not image_path_valid(mod_image_path):
            return Response({"message": "Modified image could not be found"}, status=status.HTTP_404_NOT_FOUND)

        return FileResponse(open(mod_image_path, 'rb'), content_type='image/jpeg')