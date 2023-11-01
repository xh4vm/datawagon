import enum
import uuid
from pydantic import Field, validator
from datetime import datetime as dt

from .base import JSONModel


class StatusType(str, enum.Enum):
    STARTING = 'starting'
    STOPPED = 'stopped'
    FINISHED = 'finished'
    PROCESSING = 'processing'


class Geo(JSONModel):
    latitude: float
    longitude: float


class RouteData(JSONModel):
    train_id: uuid.UUID
    railway_id: uuid.UUID
    num_railway_carriage: int
    speed: float
    status: StatusType
    datetime: dt
    geo: Geo

    @validator('speed')
    def frame_time_ge_zero(cls, value: float) -> float:
        if value >= 0:
            return value

        raise ValueError('"speed" must be greater than zero')

class StatusRoute(RouteData):
    pass
