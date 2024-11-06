import shutil
import base64
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.scripts.utility.image_processing_utility import (
    image_path_valid,
    orig_image_path,
    mod_image_path, 
    compressed_original_image_path,
    convert_image_to_pixel_array,
    convert_pixel_array_to_image
)
from api.scripts.image_resizing import (
    compress_pixel_array
)

class ResizePixelsView(APIView):
    def post(self, request):
        new_pixel_size = request.data.get("newPixelSize")

        if not new_pixel_size:
            return Response({"message": "New pixel size is required"}, status=status.HTTP_400_BAD_REQUEST)

        if not image_path_valid(orig_image_path):
            return Response({"message": "Original image could not be found"}, status=status.HTTP_404_NOT_FOUND)

        # get original image
        original_pixel_array = convert_image_to_pixel_array(orig_image_path)

        # compress original image with new size
        compressed_pixel_array = compress_pixel_array(original_pixel_array, new_pixel_size)

        # overwrite compressed original image with newly compressed image
        convert_pixel_array_to_image(compressed_pixel_array, compressed_original_image_path)

        # overwrite modified image with newly compressed image
        shutil.copyfile(compressed_original_image_path, mod_image_path)
        
        # Read the newly compressed image and encode it as base64
        with open(mod_image_path, 'rb') as compressed_image_file:
            image_data = compressed_image_file.read()
            base64_encoded_image = base64.b64encode(image_data).decode('utf-8')

        # Return encoded image
        response_data = {
            'image': base64_encoded_image,
        }

        return Response(response_data, status=status.HTTP_200_OK)
