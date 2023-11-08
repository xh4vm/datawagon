from typing import Any
from pydantic import Field

from .base import JSONModel, UUIDModelMixin, TimeStampedModelMixin


class GeoJSONType(JSONModel):
    type: str = Field(description='Тип GeoJSON', examples=['Point'])
    coordinates: list[Any] = Field(description='Координаты GeoJSON', examples=[[37.5362099,55.7668608]])


class Node(JSONModel, UUIDModelMixin, TimeStampedModelMixin):
    osm_id: str
    title: str
    location: GeoJSONType
    role: str


class Railway(JSONModel, UUIDModelMixin, TimeStampedModelMixin):
    osm_id: str
    title: str
    geo: GeoJSONType
    title_from: str
    title_to: str
    network: str
