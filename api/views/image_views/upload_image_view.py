import shutil
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.http import FileResponse
from api.scripts.image_resizing import compress_image
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
        compress_image(orig_image_path, compressed_original_image_path)

        # write compressed image to modified slot
        with open(compressed_original_image_path, 'rb') as source:
            with open(mod_image_path, 'wb+') as destination:
                shutil.copyfileobj(source, destination)

        # return compressed image
        return FileResponse(open(mod_image_path, 'rb'), content_type='image/jpeg')