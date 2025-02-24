from django.contrib import admin

from .models import App


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "status", "created_at")
    list_filter = ("status",)
    actions = ["verify_apps"]

    def verify_apps(self, request, queryset):
        queryset.update(status="verified")

    verify_apps.short_description = "Verify selected apps"
