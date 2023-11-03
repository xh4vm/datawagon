import enum
import uuid
from pydantic import validator
from datetime import datetime as dt

from .base import JSONModel
from pydantic import BaseModel, Field


class StatusType(str, enum.Enum):
    STARTING = 'starting'
    STOPPED = 'stopped'
    FINISHED = 'finished'
    PROCESSING = 'processing'


class Geo(JSONModel):
    latitude: float
    longitude: float


class RouteData(BaseModel):
    train_id: uuid.UUID
    railway_id: uuid.UUID
    num_railway_carriage: int
    speed: float
    status: StatusType
    geo: Geo

    @validator('speed')
    def frame_time_ge_zero(cls, value: float) -> float:
        if value >= 0:
            return value

        raise ValueError('"speed" must be greater than zero')

class StatusRoute(RouteData):
    datetime: str = Field(default_factory=lambda: dt.now().strftime('%Y-%m-%d %H:%M:%S'))
