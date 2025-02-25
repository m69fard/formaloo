from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class App(models.Model):
    STATUS_CHOICES = [("pending", "Pending"), ("verified", "Verified"), ("rejected", "Rejected")]

    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="pending", db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["status", "created_at"]),
            models.Index(fields=["owner", "created_at"]),
        ]

    def __str__(self):
        return self.title
