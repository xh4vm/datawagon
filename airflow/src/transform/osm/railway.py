import pandas as pd
from typing import Iterator, Any

from src.transform.base import BaseTransformer
from src.models.osm import Railway


class RailwayTransformer(BaseTransformer):
    def transform(
        self, ways: pd.DataFrame, members: pd.DataFrame, relations: pd.DataFrame, to_dict: bool = False
    ) -> Iterator[Any]:
        raw = pd.merge(ways, members, left_on="w_id", right_on="ref", how="left", suffixes=["_way", ""])
        raw = pd.merge(raw, relations, left_on="r_id", right_on="r_id", how="left", suffixes=["", "_rel"])

        for raw_elem in raw.to_dict('records'):
            elem = Railway(**raw_elem)
            yield elem.model_dump() if to_dict else elem
