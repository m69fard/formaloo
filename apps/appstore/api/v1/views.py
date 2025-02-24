from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.appstore.api.v1.serializers import AppSerializer
from apps.appstore.models import App


class AppListCreateAPIView(generics.ListCreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        return Response({"message": "List of apps (mocked)"}, status=status.HTTP_200_OK)


class PurchaseAPIView(APIView):
    def post(self, request):
        # Mock purchase logic
        return Response({"message": "Purchase successful (mocked)"}, status=status.HTTP_200_OK)
