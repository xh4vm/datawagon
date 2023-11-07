import enum
import uuid
from pydantic import validator
from datetime import datetime as dt

from .base import JSONModel
from .datetime import RangeDateTime
from pydantic import BaseModel, Field
from typing import Any


class StatusType(str, enum.Enum):
    STARTING = 'starting'
    STOPPED = 'stopped'
    FINISHED = 'finished'
    PROCESSING = 'processing'


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


class RouteData(BaseModel):
    train_id: uuid.UUID
    railway_id: uuid.UUID
    num_railway_carriage: int
    speed: float
    status: StatusType
    geo: Geo

    @validator('speed')
    def speed_ge_zero(cls, value: float) -> float:
        if value >= 0:
            return value
        
    @validator('num_railway_carriage')
    def num_ge_zero(cls, value: float) -> float:
        if value >= 0:
            return value

        raise ValueError('"num_railway_carriage" must be greater than zero')


class StatusRoute(RouteData):
    datetime: str = Field(default_factory=lambda: dt.now().strftime('%Y-%m-%d %H:%M:%S'))


class WagonType(enum.Enum):
    DANGER = 'danger'


class WagonStatus(enum.Enum):
    LOADED = 'loaded'


class Point(JSONModel):
    title: str
    geo: dict[str, Any]


class WagonData(JSONModel):
    id: uuid.UUID
    number: int
    netto: int
    status: WagonStatus
    type: WagonType
    points: list[Point]
    datetime: RangeDateTime


class TrainData(JSONModel):
    id: uuid.UUID
    wagon_counts: int
    netto: int
    brutto: int
    wagons: list[WagonData]
    route: dict[str, Any]
    railway: dict[str, Any]
