import shutil
import base64
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.http import FileResponse
from api.scripts.image_resizing import compress_image_and_return_pixel_sizes
from api.scripts.utility.image_processing_utility import (
    orig_image_path, 
    mod_image_path, 
    compressed_original_image_path
)

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file = request.FILES.get('file')

        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)
        
        # write image to original slot
        with open(orig_image_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # compress original image
        pixel_size_options = compress_image_and_return_pixel_sizes(orig_image_path, compressed_original_image_path)

        # write compressed image to modified slot
        with open(compressed_original_image_path, 'rb') as source:
            with open(mod_image_path, 'wb+') as destination:
                shutil.copyfileobj(source, destination)

        # Read the compressed image and encode it as base64
        with open(mod_image_path, 'rb') as compressed_image_file:
            image_data = compressed_image_file.read()
            base64_encoded_image = base64.b64encode(image_data).decode('utf-8')

        # Return encoded image and options
        response_data = {
            'image': base64_encoded_image,
            'pixel_size_options': pixel_size_options
        }

        return Response(response_data, status=status.HTTP_200_OK)