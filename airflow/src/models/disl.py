import uuid
from pydantic import Field
from datetime import datetime as dt

from src.models.base import JSONModel


class DislData(JSONModel):
    wagnum: int
    operdate: dt = Field(default_factory=dt.utcnow)
    st_id_disl: int
    st_id_dest: int
    train_index: str

    def __init__(self, operdate: dt, **kwargs) -> None:
        super().__init__(
            **kwargs
        )

class TrainDislData(DislData):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False)
    train_st_start: int | None
    train_st_num: int
    train_st_end: int | None
    datetime: dt = Field(default_factory=dt.utcnow)
    created_at: dt = Field(default_factory=dt.utcnow)
    
    def __init__(self, train_index: str, **kwargs) -> None:
        train_st_start, train_st_num, train_st_end = train_index.split('-')
        super().__init__(
            train_index=train_index,
            train_st_start=train_st_start if train_st_start != '' else 0,
            train_st_num=train_st_num,
            train_st_end=train_st_end if train_st_end != '' else 0,
            **kwargs
        )
