from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from apps.appstore.models import App


class AppTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_create_app(self):
        url = reverse("app-list-create")
        response = self.client.post(
            url,
            {"title": "Test App", "description": "This is a test app", "price": "99.99"},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(App.objects.get().owner, self.user)
        self.assertEqual(App.objects.count(), 1)
