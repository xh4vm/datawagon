import pandas.io.sql as psql
import backoff
import pandas as pd
from loguru import logger
from psycopg2 import connect as pg_connect
from psycopg2.extras import DictCursor

from src.core.config import BACKOFF_CONFIG, POSTGRES, PostgresSettings
from .base import BaseExtractor


class PostgresExtractor(BaseExtractor):
    def __init__(
        self,
        settings: PostgresSettings = POSTGRES
    ):
        self._settings = settings
        self.conn = None

    def __enter__(self):
        self.conn = pg_connect(**self._settings.dsl(), cursor_factory=DictCursor)
        return self

    def __exit__(self, *args, **kwargs):
        self.conn.close()

    # @backoff.on_exception(**BACKOFF_CONFIG, logger=logger)
    def extract(self, query: str) -> pd.DataFrame:
        return psql.read_sql_query(f"{query}", self.conn)
