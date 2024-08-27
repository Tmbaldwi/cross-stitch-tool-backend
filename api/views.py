from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TestTable
from .serializers import TestTableSerializer
from django.db import connection

class TestTableView(APIView):
    def get(self, request):
        # Data Retrieval
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM test_function()")
            results = cursor.fetchall()

        if results:
            data = [
                {"id": row[0], "testname": row[1], "addr": row[2]}
                for row in results
            ]

            # Serialization
            serializer = TestTableSerializer(data, many=True)

            return Response(serializer.data)

        # Response
        return Response({"error": "No data found"}, status=404)