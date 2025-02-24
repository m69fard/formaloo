from django.urls import include, path
from rest_framework import routers

from .views import AppListCreateAPIView, PurchaseAPIView

urlpatterns = [
    path("apps", AppListCreateAPIView.as_view(), name="app-list-create"),
    path("purchase", PurchaseAPIView.as_view(), name="purchase"),
]
