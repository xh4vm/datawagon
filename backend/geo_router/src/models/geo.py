from pydantic import Field, validator
from datetime import datetime
from typing import Any

from .base import JSONModel


class Geo(JSONModel):
    latitude: float
    longitude: float

    @validator('latitude')
    def latitude_ge_zero(cls, value: float) -> float:
        if value >= 0:
            return value

        raise ValueError('"latitude" must be greater than zero')
    
    @validator('longitude')
    def longitude_ge_zero(cls, value: float) -> float:
        if value >= 0:
            return value

        raise ValueError('"longitude" must be greater than zero')


class GeoJSONType(JSONModel):
    type: str = Field(description='Тип GeoJSON', examples=['Point'])
    coordinates: list[Any] = Field(description='Координаты GeoJSON', examples=[[37.5362099,55.7668608]])


class GeoPoint(JSONModel):
    title: str = Field(description='Имя гео точки', examples=['Дмитров'])
    geo: dict

class GeoPointOperdate(GeoPoint):
    operdate: datetime
