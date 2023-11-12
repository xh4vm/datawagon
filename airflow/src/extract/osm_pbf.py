from dataclasses import dataclass
import osmium
import pandas as pd
import numpy as np
from loguru import logger

from src.core.config import OSMSettings
from src.extract.base import BaseExtractor


@dataclass
class OSMPBFExtractor(BaseExtractor):
    osm_file: str
    handler: osmium.SimpleHandler
    csv_file_path: str

    def create_mapping(self):
        csv_data = pd.read_csv(self.csv_file_path)

        # Проверка наличия столбцов
        required_columns = {'OSM_ID', 'ST_ID'}
        if not required_columns.issubset(csv_data.columns):
            missing_columns = required_columns - set(csv_data.columns)
            raise ValueError(f"Отсутствуют обязательные столбцы: {missing_columns}")

        # Переименование столбца OSM_ID и конвертация в int
        csv_data = csv_data.rename(columns={'OSM_ID': 'n_id'}).dropna()
        csv_data['n_id'] = csv_data['n_id'].astype(int)

        return csv_data[['n_id', 'ST_ID']]

    def extract(self) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        # Прочитать данные из CSV файла и загрузить их в pandas DataFrame
        # csv_data = self.create_mapping()

        self.handler.apply_file(self.osm_file, locations=True, idx='flex_mem')

        nodes, ways, relation_members, relations = (
            pd.DataFrame(self.handler.nodes).replace(np.nan, None),
            pd.DataFrame(self.handler.ways).replace(np.nan, None),
            pd.DataFrame(self.handler.relation_members).replace(np.nan, None),
            pd.DataFrame(self.handler.relations).replace(np.nan, None),
        )

        # # Используем маппинг из DataFrame для обогащения данных
        # if 'n_id' in nodes.columns:
        #     nodes['n_id'] = nodes['n_id'].astype(int)
        #     nodes = pd.merge(nodes, csv_data, how='left', left_on='n_id', right_on='n_id').replace(np.nan, None)


        return nodes, ways, relation_members, relations
