from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('administration.urls')),
    path("package/", include('vacation_package.urls')),
]
