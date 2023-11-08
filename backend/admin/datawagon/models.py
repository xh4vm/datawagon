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
    title = models.CharField(_("title"), max_length=4096, blank=True, null=True)
    role = models.CharField(_("role"), max_length=128, blank=True, null=True)
    location = models.PointField(_("location"), blank=False, null=False)

    class Meta:
        db_table = 'content"."nodes'
        verbose_name = _("Node")
        verbose_name_plural = _("Nodes")


class Railway(UUIDMixin, TimeStampedMixin):
    title = models.CharField(_("title"), max_length=4096, blank=True, null=True)
    title_from = models.CharField(_("title_from"), max_length=512, blank=True, null=True)
    title_to = models.CharField(_("title_to"), max_length=512, blank=True, null=True)
    network = models.CharField(_("network"), max_length=512, blank=True, null=True)
    geo = models.MultiLineStringField(_("geo"), blank=False, null=False)

    class Meta:
        db_table = 'content"."railways'
        verbose_name = _("Railway")
        verbose_name_plural = _("Railways")
