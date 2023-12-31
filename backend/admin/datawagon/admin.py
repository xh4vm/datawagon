from django.contrib.gis import admin
from django.db.models import F, Prefetch
from django.utils.translation import gettext_lazy as _

from .models import Train, Wagon, Node, Railway, RailwayNode


class WagonInline(admin.TabularInline):
    model = Wagon


@admin.register(Wagon)
class WagonAdmin(admin.ModelAdmin):
    list_display = ("train_id", "number")
    search_fields = ("number",)


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("title",)

    inlines = (WagonInline,)


class CustomGeoWidgetAdmin(admin.GISModelAdmin):
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 9,
            "default_lon": 37.7495,
            "default_lat": 55.7474,
        },
    }


@admin.register(Node)
class NodeAdmin(CustomGeoWidgetAdmin):
    list_display = ("title", "role", "location", "station_id")
    search_fields = (
        "title",
        "role",
        "station_id",
    )


@admin.register(Railway)
class RailwayAdmin(CustomGeoWidgetAdmin):
    list_display = (
        "title",
        "title_from",
        "title_to",
        "network",
        "geo",
    )
    search_fields = (
        "title",
        "title_from",
        "title_to",
        "network",
    )


@admin.register(RailwayNode)
class RailwayNodeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "node_osm_id",
        "railway_osm_id",
    )
    search_fields = (
        "id",
        "node_osm_id",
        "railway_osm_id",
    )
