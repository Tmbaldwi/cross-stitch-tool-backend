from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TestTable
from .serializers import TestTableSerializer

class TestTableView(APIView):
    def get(self, request):
        # Data Retrieval
        first_entry = TestTable.objects.first()  # Retrieves the first record from test_table

        # Serialization
        serializer = TestTableSerializer(first_entry)

        # Response
        return Response(serializer.data)