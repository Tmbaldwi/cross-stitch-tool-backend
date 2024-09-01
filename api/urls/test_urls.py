from django.urls import path
from ..views.test_view import TestTableView

urlpatterns = [
    path('', TestTableView.as_view(), name='test-table')
]