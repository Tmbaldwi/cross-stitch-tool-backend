# backend/api/urls.py

from django.urls import path
from .views import TestTableView

urlpatterns = [
    path('test/', TestTableView.as_view(), name='test-table'),
]