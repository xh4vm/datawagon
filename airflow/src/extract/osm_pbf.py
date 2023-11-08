from dataclasses import dataclass
from typing import Any
import osmium
import pandas as pd

from src.core.config import OSMSettings
from src.extract.base import BaseExtractor


@dataclass
class OSMPBFExtractor(BaseExtractor):
    osm_config: OSMSettings
    handler: osmium.SimpleHandler

    def extract(self) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        self.handler.apply_file(self.osm_config.FILE, locations=True, idx='flex_mem')

        return pd.DataFrame(self.handler.nodes), pd.DataFrame(self.handler.ways), pd.DataFrame(self.handler.relation_members), pd.DataFrame(self.handler.relations)
