import enum
import uuid
from pydantic import validator, BaseModel, Field
from datetime import datetime as dt

from .geo import Geo


class StatusType(str, enum.Enum):
    STARTING = 'starting'
    STOPPED = 'stopped'
    FINISHED = 'finished'
    PROCESSING = 'processing'


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
