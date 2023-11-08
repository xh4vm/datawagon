from typing import Any, Dict

import backoff
from pydantic import Field
from pydantic_settings import BaseSettings


class PostgresSettings(BaseSettings):
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int
    NAME: str

    class Config:
        env_prefix = "DB_"

    def dsl(self) -> Dict[str, Any]:
        return {
            "dbname": self.NAME,
            "user": self.USER,
            "password": self.PASSWORD,
            "host": self.HOST,
            "port": self.PORT,
        }


class RedisSettings(BaseSettings):
    PASSWORD: str
    HOST: str
    PORT: int
    CACHE_EXPIRE: int

    class Config:
        env_prefix = "REDIS_"


class ClickhouseSettings(BaseSettings):
    NODES: str
    INIT_TABLE: str
    INIT_DATA: bool = Field(False)
    INIT_DATA_PATH: str | None

    @classmethod
    def parse_env_var(cls, field_name: str, raw_val: str) -> Any:
        if field_name.upper() == "NODES":
            return [x for x in raw_val.split(",")]
        return cls.json_loads(raw_val)

    class Config:
        env_prefix = "CH_"


class StatusRouteSettingsNode01(BaseSettings):
    DISTRIBUTED_TABLE: str
    REPLICA_PATH: str
    REPLICA_NAME: str

    class Config:
        env_prefix = "CLICKHOUSE_NODE01_STATUS_ROUTE_"


class ClickhouseNode01(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    CLUSTER: str
    STATUS_ROUTE: BaseSettings = Field(default_factory=StatusRouteSettingsNode01)

    class Config:
        env_prefix = "CLICKHOUSE_NODE01_"


class StatusRouteSettingsNode02(BaseSettings):
    DISTRIBUTED_TABLE: str
    REPLICA_PATH: str
    REPLICA_NAME: str

    class Config:
        env_prefix = "CLICKHOUSE_NODE02_STATUS_ROUTE_"


class ClickhouseNode02(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    CLUSTER: str
    STATUS_ROUTE: BaseSettings = Field(default_factory=StatusRouteSettingsNode02)

    class Config:
        env_prefix = "CLICKHOUSE_NODE02_"


class StatusRouteSettingsNode03(BaseSettings):
    DISTRIBUTED_TABLE: str
    REPLICA_PATH: str
    REPLICA_NAME: str

    class Config:
        env_prefix = "CLICKHOUSE_NODE03_STATUS_ROUTE_"


class ClickhouseNode03(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    CLUSTER: str
    STATUS_ROUTE: BaseSettings = Field(default_factory=StatusRouteSettingsNode03)

    class Config:
        env_prefix = "CLICKHOUSE_NODE03_"


class StatusRouteSettingsNode04(BaseSettings):
    DISTRIBUTED_TABLE: str
    REPLICA_PATH: str
    REPLICA_NAME: str

    class Config:
        env_prefix = "CLICKHOUSE_NODE04_STATUS_ROUTE_"


class ClickhouseNode04(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    CLUSTER: str
    STATUS_ROUTE: BaseSettings = Field(default_factory=StatusRouteSettingsNode04)

    class Config:
        env_prefix = "CLICKHOUSE_NODE04_"


class StatusRouteSettingsNode05(BaseSettings):
    DISTRIBUTED_TABLE: str
    REPLICA_PATH: str
    REPLICA_NAME: str

    class Config:
        env_prefix = "CLICKHOUSE_NODE05_STATUS_ROUTE_"


class ClickhouseNode05(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    CLUSTER: str
    STATUS_ROUTE: BaseSettings = Field(default_factory=StatusRouteSettingsNode05)

    class Config:
        env_prefix = "CLICKHOUSE_NODE05_"


class StatusRouteSettingsNode06(BaseSettings):
    DISTRIBUTED_TABLE: str
    REPLICA_PATH: str
    REPLICA_NAME: str

    class Config:
        env_prefix = "CLICKHOUSE_NODE06_STATUS_ROUTE_"


class ClickhouseNode06(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    CLUSTER: str
    STATUS_ROUTE: BaseSettings = Field(default_factory=StatusRouteSettingsNode06)

    class Config:
        env_prefix = "CLICKHOUSE_NODE06_"


NODES = [
    ClickhouseNode01(),
    ClickhouseNode02(),
    ClickhouseNode03(),
    ClickhouseNode04(),
    ClickhouseNode05(),
    ClickhouseNode06(),
]

CLICKHOUSE_CONFIG: ClickhouseSettings = ClickhouseSettings()

REDIS_CONFIG = RedisSettings()
POSTGRES_CONFIG = PostgresSettings()


BACKOFF_CONFIG: Dict[str, Any] = {
    "wait_gen": backoff.expo,
    "exception": Exception,
    "max_value": 8,
}
