import pandas as pd
from typing import Any, Iterator
from loguru import logger

from src.transform.base import BaseTransformer
from src.models.disl import TrainDislData


class DislTransformer(BaseTransformer):
    def transform(
        self, disls: pd.DataFrame, to_dict: bool = False
    ) -> Iterator[Any]:
        
        disls = disls.dropna().rename(columns={
            column: column.lower() for column in disls.columns
        })
        
        for _, raw_elem in disls.iterrows():
            elem = TrainDislData(**raw_elem)
            yield elem.model_dump() if to_dict else elem
