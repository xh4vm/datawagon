from django.contrib.gis import admin, forms
from django.db.models import F, Prefetch
from django.utils.translation import gettext_lazy as _
from dal import autocomplete

from .models import Train, Wagon, Node, Railway, RailwayNode, Waybill


class CustomGeoWidgetAdmin(admin.GISModelAdmin):
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 9,
            'default_lon': 37.7495,
            'default_lat': 55.7474,
        },
    }


@admin.register(Node)
class NodeAdmin(CustomGeoWidgetAdmin):
    list_display = ("title", "role", "location")
    search_fields = ("title", "role",)


@admin.register(Railway)
class RailwayAdmin(CustomGeoWidgetAdmin):
    list_display = ("title", "title_from", "title_to", "network", "geo",)
    search_fields = ("title", "title_from", "title_to", "network",)


@admin.register(RailwayNode)
class RailwayNodeAdmin(admin.ModelAdmin):
    list_display = ("id", "node_osm_id", "railway_osm_id",)
    search_fields = ("id", "node_osm_id", "railway_osm_id",)


class RailwayForm(forms.ModelForm):
    class Meta:
        model = Railway
        fields = ('__all__')
        widgets = {
            'title': autocomplete.ModelSelect2(url='railway-autocomplete')
        }


class RailwayInline(admin.TabularInline):
    model = Train.railways.through
    form = RailwayForm


class WagonInline(admin.TabularInline):
    model = Wagon


@admin.register(Wagon)
class WagonAdmin(admin.ModelAdmin):
    list_display = ("train_id", "number")
    search_fields = ("number",)


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ("get_railway_title",)
    search_fields = ("get_railway_title",)

    inlines = (RailwayInline,)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        railway_prefetch = Prefetch(
            "railways",
            to_attr="_railway",
            queryset=(Railway.objects.all()),
        )

        return queryset.prefetch_related(railway_prefetch)
    
    @admin.display(description=_('Railway title'))
    def get_railway_title(self, train):
        return '; '.join([railway.title for railway in train._railway])


@admin.register(Waybill)
class WaybillAdmin(CustomGeoWidgetAdmin):
    list_display = ("number", "start_node_id", "finish_node_id", "geo",)
    search_fields = ("number", "start_node_id", "finish_node_id",)
    autocomplete_fields = ("start_node_id", "finish_node_id",)
