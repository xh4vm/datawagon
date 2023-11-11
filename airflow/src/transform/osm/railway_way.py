import pandas as pd
from typing import Iterator, Any

from src.transform.base import BaseTransformer
from src.models.osm import RailwayWayData


class RailwayNodeTransformer(BaseTransformer):
    def transform(
        self, members: pd.DataFrame, to_dict: bool = False
    ) -> Iterator[Any]:

        for raw_elem in members[members.type == 'w'].iterrows():

            elem = RailwayWayData(
                way_osm_id=raw_elem[1]["ref"],
                railway_osm_id=raw_elem[1]["r_id"],
            )

            yield elem.model_dump() if to_dict else elem
