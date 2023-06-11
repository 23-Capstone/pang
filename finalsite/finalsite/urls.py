from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("pang/", include("pang.urls")),
    path("admin/", admin.site.urls),
]
