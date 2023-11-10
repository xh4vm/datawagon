import pandas as pd
from typing import Iterator, Any
from shapely import to_geojson

from src.transform.base import BaseTransformer
from src.models.osm import WayData


class WayTransformer(BaseTransformer):
    def transform(
        self, ways: pd.DataFrame, to_dict: bool = False
    ) -> Iterator[Any]:
        for raw_elem in ways.iterrows():

            elem = WayData(
                osm_id=raw_elem[1]['w_id'],
                geo=to_geojson(raw_elem[1]['geo']),
            )
            yield elem.model_dump() if to_dict else elem
