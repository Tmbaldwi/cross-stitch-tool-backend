from rest_framework import serializers
from .models.test_models import TestTable

class TestTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestTable
        fields = ['id', 'testname', 'addr']