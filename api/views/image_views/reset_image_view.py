import os
import shutil
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse
from api.scripts.utility.image_processing_utility import image_path_valid

current_dir = os.path.dirname(os.path.abspath(__file__))

mod_image_path = os.path.join(current_dir, '..', '..', '..', 'media', 'modified_image.png')
orig_image_path = os.path.join(current_dir, '..', '..', '..', 'media', 'original_image.png')


class ResetImageView(APIView):
    def post(self, request):
        
        if not image_path_valid(mod_image_path):
            return Response({"message": "Modified image could not be found"}, status=status.HTTP_404_NOT_FOUND)
        
        if not image_path_valid(orig_image_path):
            return Response({"message": "Original image could not be found"}, status=status.HTTP_404_NOT_FOUND)

        shutil.copyfile(orig_image_path, mod_image_path)

        return FileResponse(open(mod_image_path, 'rb'), content_type='image/jpeg')