from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file = request.FILES.get('file')

        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)
        
        with open(f'media/{"original_image.png"}', 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        with open(f'media/{"modified_image.png"}', 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        return Response({"message": "Image uploaded successfully"}, status=status.HTTP_200_OK)