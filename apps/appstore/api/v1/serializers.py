from rest_framework import serializers

from apps.appstore.models import App


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = [
            "id",
            "title",
            "description",
            "price",
            "owner",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["owner", "status"]
