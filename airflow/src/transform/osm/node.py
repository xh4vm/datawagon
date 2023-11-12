import pandas as pd
from typing import Iterator, Any
from shapely import to_geojson
from loguru import logger

from src.transform.base import BaseTransformer
from src.models.osm import NodeData


class NodeTransformer(BaseTransformer):
    def transform(self, nodes: pd.DataFrame, to_dict: bool = False) -> Iterator[Any]:
        for _, raw_elem in nodes.iterrows():
            elem = NodeData(
                osm_id=raw_elem["n_id"],
                title=raw_elem["name"],
                location=to_geojson(raw_elem["geo"]),
                role=raw_elem["railway"],
                station_id=raw_elem.get("ST_ID"),
            )

            yield elem.model_dump() if to_dict else elem
