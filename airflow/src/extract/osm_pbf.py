from dataclasses import dataclass
import osmium
import pandas as pd
import numpy as np

from src.core.config import OSMSettings
from src.extract.base import BaseExtractor


@dataclass
class OSMPBFExtractor(BaseExtractor):
    osm_config: OSMSettings
    handler: osmium.SimpleHandler

    def extract(self) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        self.handler.apply_file(self.osm_config.FILE, locations=True, idx='flex_mem')

        return (
            pd.DataFrame(self.handler.nodes).replace(np.nan, None),
            pd.DataFrame(self.handler.ways).replace(np.nan, None),
            pd.DataFrame(self.handler.relation_members).replace(np.nan, None),
            pd.DataFrame(self.handler.relations).replace(np.nan, None),
        )
