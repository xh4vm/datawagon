import orjson
import uuid

from datetime import datetime
from pydantic import BaseModel, Field


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class JSONModel(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
        use_enum_values = True


class UUIDModelMixin(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, nullable=False)


class TimeStampedModelMixin(BaseModel):
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
