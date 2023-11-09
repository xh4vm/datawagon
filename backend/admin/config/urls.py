from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("panel/__debug__/", include("debug_toolbar.urls")),
    path("panel/admin/", admin.site.urls),
]
