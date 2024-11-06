import shutil
import base64
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.scripts.utility.image_processing_utility import (
    image_path_valid, 
    mod_image_path, 
    compressed_original_image_path
)


class ResetImageView(APIView):
    def post(self, request):
        
        if not image_path_valid(mod_image_path):
            return Response({"message": "Modified image could not be found"}, status=status.HTTP_404_NOT_FOUND)
        
        if not image_path_valid(compressed_original_image_path):
            return Response({"message": "Compressed original image could not be found"}, status=status.HTTP_404_NOT_FOUND)

        shutil.copyfile(compressed_original_image_path, mod_image_path)

        # Read the compressed image and encode it as base64
        with open(mod_image_path, 'rb') as compressed_image_file:
            image_data = compressed_image_file.read()
            base64_encoded_image = base64.b64encode(image_data).decode('utf-8')

        # Return encoded image
        response_data = {
            'image': base64_encoded_image,
        }

        return Response(response_data, status=status.HTTP_200_OK)