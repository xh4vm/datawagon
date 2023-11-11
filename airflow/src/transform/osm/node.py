import pandas as pd
from typing import Iterator, Any
from loguru import logger
from shapely import to_geojson
from shapely.geometry import Point

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
                role=raw_elem[1]['railway']
            )
            yield elem.model_dump() if to_dict else elem
