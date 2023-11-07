from datetime import datetime
from pydantic import validator

from .base import JSONModel


class RangeDateTime(JSONModel):
    start: str
    end: str

    @validator('start')
    def start_format(cls, value: str) -> datetime:
        return datetime.strptime(value, '%Y-%m-%d')


    @validator('end')
    def end_format(cls, value: str) -> datetime:
        return datetime.strptime(value, '%Y-%m-%d')
