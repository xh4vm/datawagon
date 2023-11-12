import pandas as pd
from typing import Any, Iterator

from src.transform.base import BaseTransformer
from src.models.station import StationData


class StationTransformer(BaseTransformer):
    def transform(self, stations: pd.DataFrame, to_dict: bool = False) -> Iterator[Any]:
        stations = stations.dropna().rename(
            columns={column: column.lower() for column in stations.columns}
        )

        for _, raw_elem in stations.iterrows():
            elem = StationData(station_id=raw_elem["st_id"], osm_id=raw_elem["osm_id"])
            yield elem.model_dump() if to_dict else elem
