import pandas as pd
from dataclasses import dataclass

from src.extract.base import BaseExtractor


@dataclass
class ExcelExtractor(BaseExtractor):
    path: str

    def extract(self) -> pd.DataFrame:
        return pd.read_excel(self.path)
