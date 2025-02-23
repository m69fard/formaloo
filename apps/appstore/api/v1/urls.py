from django.urls import include, path
from rest_framework import routers

from .views import AppCreateAPIView

urlpatterns = [
    path("apps", AppCreateAPIView.as_view(), name="app-create"),
]
