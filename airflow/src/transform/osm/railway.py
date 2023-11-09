import pandas as pd
from typing import Iterator, Any
import geopandas as gpd
from shapely import to_geojson
from shapely.geometry import MultiLineString

from src.transform.base import BaseTransformer
from src.models.osm import RailwayData


class RailwayTransformer(BaseTransformer):
    def transform(
        self, ways: pd.DataFrame, members: pd.DataFrame, relations: pd.DataFrame, to_dict: bool = False
    ) -> Iterator[Any]:
        raw = pd.merge(ways, members, left_on="w_id", right_on="ref", how="left", suffixes=["_way", ""])
        raw = pd.merge(raw, relations, left_on="r_id", right_on="r_id", how="left", suffixes=["", "_rel"])

        gdf = gpd.GeoDataFrame(raw, geometry="geo")

        for raw_elem in relations.iterrows():
            r_id = raw_elem[1]["r_id"]
            mline = MultiLineString(gdf[gdf.r_id == r_id].geo.array)

            elem = RailwayData(
                osm_id=r_id,
                title=raw_elem[1]["name"],
                geo=to_geojson(mline),
                title_from=raw_elem[1]["from"],
                title_to=raw_elem[1]["to"],
                operator=raw_elem[1]["operator"],
                network=raw_elem[1]["network"],
            )

            yield elem.model_dump() if to_dict else elem
