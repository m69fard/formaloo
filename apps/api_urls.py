from django.urls import include, path

urlpatterns = [
    path("v1/appstore/", include("apps.appstore.api.v1.urls")),
]
