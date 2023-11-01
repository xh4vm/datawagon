from pydantic import Field
from pydantic_settings import BaseSettings


class StatusRouteSettingsNode01(BaseSettings):
    DISTRIBUTED_TABLE: str = Field(..., env="CH_STATUS_ROUTE_DISTRIBUTED_TABLE")
    REPLICA_PATH: str
    REPLICA_NAME: str

    class Config:
        env_prefix = "CLICKHOUSE_NODE01_STATUS_ROUTE_"


class ClickhouseNode01(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    CLUSTER: str = Field(..., env="CH_CLUSTER_NAME")
    STATUS_ROUTE: BaseSettings = Field(default_factory=StatusRouteSettingsNode01)

    class Config:
        env_prefix = "CLICKHOUSE_NODE01_"


class StatusRouteSettingsNode02(BaseSettings):
    DISTRIBUTED_TABLE: str = Field(..., env="CH_STATUS_ROUTE_DISTRIBUTED_TABLE")
    REPLICA_PATH: str
    REPLICA_NAME: str

    class Config:
        env_prefix = "CLICKHOUSE_NODE02_STATUS_ROUTE_"


class ClickhouseNode02(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    CLUSTER: str = Field(..., env="CH_CLUSTER_NAME")
    STATUS_ROUTE: BaseSettings = Field(default_factory=StatusRouteSettingsNode02)

    class Config:
        env_prefix = "CLICKHOUSE_NODE02_"


class StatusRouteSettingsNode03(BaseSettings):
    DISTRIBUTED_TABLE: str = Field(..., env="CH_STATUS_ROUTE_DISTRIBUTED_TABLE")
    REPLICA_PATH: str
    REPLICA_NAME: str

    class Config:
        env_prefix = "CLICKHOUSE_NODE03_STATUS_ROUTE_"


class ClickhouseNode03(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    CLUSTER: str = Field(..., env="CH_CLUSTER_NAME")
    STATUS_ROUTE: BaseSettings = Field(default_factory=StatusRouteSettingsNode03)

    class Config:
        env_prefix = "CLICKHOUSE_NODE03_"


class StatusRouteSettingsNode04(BaseSettings):
    DISTRIBUTED_TABLE: str = Field(..., env="CH_STATUS_ROUTE_DISTRIBUTED_TABLE")
    REPLICA_PATH: str
    REPLICA_NAME: str

    class Config:
        env_prefix = "CLICKHOUSE_NODE04_STATUS_ROUTE_"


class ClickhouseNode04(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    CLUSTER: str = Field(..., env="CH_CLUSTER_NAME")
    STATUS_ROUTE: BaseSettings = Field(default_factory=StatusRouteSettingsNode04)

    class Config:
        env_prefix = "CLICKHOUSE_NODE04_"


class StatusRouteSettingsNode05(BaseSettings):
    DISTRIBUTED_TABLE: str = Field(..., env="CH_STATUS_ROUTE_DISTRIBUTED_TABLE")
    REPLICA_PATH: str
    REPLICA_NAME: str

    class Config:
        env_prefix = "CLICKHOUSE_NODE05_STATUS_ROUTE_"


class ClickhouseNode05(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    CLUSTER: str = Field(..., env="CH_CLUSTER_NAME")
    STATUS_ROUTE: BaseSettings = Field(default_factory=StatusRouteSettingsNode05)

    class Config:
        env_prefix = "CLICKHOUSE_NODE05_"


class StatusRouteSettingsNode06(BaseSettings):
    DISTRIBUTED_TABLE: str = Field(..., env="CH_STATUS_ROUTE_DISTRIBUTED_TABLE")
    REPLICA_PATH: str
    REPLICA_NAME: str

    class Config:
        env_prefix = "CLICKHOUSE_NODE06_STATUS_ROUTE_"


class ClickhouseNode06(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    CLUSTER: str = Field(..., env="CH_CLUSTER_NAME")
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
