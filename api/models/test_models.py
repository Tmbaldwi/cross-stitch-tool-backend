from django.db import models

class TestTable(models.Model):
    id = models.AutoField(primary_key=True)
    testname = models.CharField(max_length=100)
    addr = models.TextField()

    class Meta:
        db_table = 'test_table'
