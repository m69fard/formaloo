from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Mock login logic
        return Response({"message": "Login successful (mocked)"}, status=status.HTTP_200_OK)


class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Mock signup logic
        return Response({"message": "Signup successful (mocked)"}, status=status.HTTP_201_CREATED)
