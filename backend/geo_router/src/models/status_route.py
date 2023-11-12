from pydantic import validator, BaseModel, Field
from datetime import datetime as dt


class RouteData(BaseModel):
    wagnum: int
    operdate: str
    st_id_disl: int
    st_id_dest: int
    train_index: str

    @validator("operdate")
    def operdate_validate(cls, value: str) -> str:
        if isinstance(dt.strptime(value, "%Y-%m-%d %H:%M:%S"), dt):
            return value


class StatusRoute(RouteData):
    train_st_start: int
    train_st_num: int
    train_st_end: int
    datetime: str = Field(
        default_factory=lambda: dt.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    def __init__(self, train_index: str, **kwargs) -> None:
        train_st_start, train_st_num, train_st_end = train_index.split("-")
        super().__init__(
            train_index=train_index,
            train_st_start=train_st_start,
            train_st_num=train_st_num,
            train_st_end=train_st_end,
            **kwargs
        )
