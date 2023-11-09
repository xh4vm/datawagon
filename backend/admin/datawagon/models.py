from uuid import uuid4

from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True


class Wagon(UUIDMixin, TimeStampedMixin):
    train = models.ForeignKey(
        "Train", 
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name="wagons",
        verbose_name=_("Train"),
    )
    number = models.IntegerField(_("number"), blank=True, null=True)

    class Meta:
        db_table = 'content"."wagons'
        verbose_name = _("Wagon")
        verbose_name_plural = _("Wagons")


class Train(UUIDMixin, TimeStampedMixin):

    class Meta:
        db_table = 'content"."trains'
        verbose_name = _("Train")
        verbose_name_plural = _("Train")


class Node(UUIDMixin, TimeStampedMixin):
    osm_id = models.BigIntegerField(_("osm_id"), blank=False, null=False, unique=True)
    title = models.CharField(_("title"), max_length=4096, blank=True, null=True)
    role = models.CharField(_("role"), max_length=128, blank=True, null=True)
    location = models.PointField(_("location"), blank=False, null=False)

    class Meta:
        db_table = 'content"."nodes'
        verbose_name = _("Node")
        verbose_name_plural = _("Nodes")

    def __str__(self):
        return self.title


class Railway(UUIDMixin, TimeStampedMixin):
    osm_id = models.BigIntegerField(_("osm_id"), blank=False, null=False, unique=True)
    title = models.CharField(_("title"), max_length=4096, blank=True, null=True)
    title_from = models.CharField(_("title_from"), max_length=512, blank=True, null=True)
    title_to = models.CharField(_("title_to"), max_length=512, blank=True, null=True)
    operator = models.CharField(_("operator"), max_length=512, blank=True, null=True)
    network = models.CharField(_("network"), max_length=512, blank=True, null=True)
    geo = models.MultiLineStringField(_("geo"), blank=False, null=False)

    class Meta:
        db_table = 'content"."railways'
        verbose_name = _("Railway")
        verbose_name_plural = _("Railways")

    def __str__(self):
        return self.title


class RailwayNode(UUIDMixin, TimeStampedMixin):
    node_osm_id = models.ForeignKey(
        "Node", 
        null=True, blank=True,
        to_field='osm_id',
        db_column='node_osm_id',
        on_delete=models.CASCADE,
        verbose_name=_("Node"),
    )
    railway_osm_id = models.ForeignKey(
        "Railway",
        null=True, blank=True,
        to_field='osm_id',
        db_column='railway_osm_id',
        on_delete=models.CASCADE,
        verbose_name=_("Railway"),
    )

    class Meta:
        db_table = 'content"."railway_nodes'
        verbose_name = _("RailwayNode")
        verbose_name_plural = _("RailwayNodes")
