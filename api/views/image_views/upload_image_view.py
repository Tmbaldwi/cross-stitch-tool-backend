from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from api.scripts.image_resizing import compress_image
from api.scripts.utility.image_processing_utility import orig_image_path, mod_image_path, compressed_original_image_path

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file = request.FILES.get('file')

        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)
        
        # write image to original slot
        with open(f'media/{"original_image.png"}', 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # compress original image
        compress_image(orig_image_path, compressed_original_image_path)

        # write image to modified slot TODO write compressed image to modified slot
        with open(f'media/{"modified_image.png"}', 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # return compressed image

        return Response({"message": "Image uploaded successfully"}, status=status.HTTP_200_OK)