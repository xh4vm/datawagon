from dal import autocomplete
from django.contrib import admin
from django.urls import include, path, re_path as url
from datawagon.models import Railway

urlpatterns = [
    path("panel/__debug__/", include("debug_toolbar.urls")),
    path("panel/admin/", admin.site.urls),
    url(
        'railway-autocomplete/$',
        autocomplete.Select2QuerySetView.as_view(model=Railway),
        name='select2_fk',
    ),
]
