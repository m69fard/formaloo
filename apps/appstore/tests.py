from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.appstore.models import App

User = get_user_model()


class TestAppAdmin(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username="admin", password="admin")
        self.client.login(username="admin", password="admin")
        self.app1 = App.objects.create(
            title="Test App1", description="test description", price=5.99, owner=self.admin_user
        )
        self.app2 = App.objects.create(
            title="Test App2", description="test description", price=19.99, owner=self.admin_user
        )
        self.app3 = App.objects.create(
            title="Test App3", description="test description", price=3.99, owner=self.admin_user
        )

    def test_admin_verification(self):
        data = {"action": "verify_apps", "_selected_action": [self.app1.pk, self.app3.pk]}
        url = reverse("admin:appstore_app_changelist")
        self.client.post(url, data)
        self.assertEqual(App.objects.get(pk=self.app1.pk).status, "verified")
        self.assertEqual(App.objects.get(pk=self.app2.pk).status, "pending")
        self.assertEqual(App.objects.get(pk=self.app3.pk).status, "verified")
