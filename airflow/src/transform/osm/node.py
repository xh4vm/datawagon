import pandas as pd
from typing import Iterator, Any
from shapely import to_geojson

from src.transform.base import BaseTransformer
from src.models.osm import NodeData


class NodeTransformer(BaseTransformer):
    def transform(
        self, nodes: pd.DataFrame, to_dict: bool = False
    ) -> Iterator[Any]:
        for raw_elem in nodes.iterrows():

            elem = NodeData(
                osm_id=raw_elem[1]['n_id'],
                st_id= raw_elem[1]['ST_ID'],
                title=raw_elem[1]['name'],
                location=to_geojson(raw_elem[1]['geo']),
                role=raw_elem[1]['railway'],
                station_id=raw_elem[1].get('st_id')
            )
            yield elem.model_dump() if to_dict else elem
