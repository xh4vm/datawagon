import logging
from logging import config as logging_config

from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    HOST: str = Field('localhost')
    PORT: int
    PROJECT_NAME: str
    API_PATH: str
    API_URL: str
    SCHEMA_REGISTRY_URL: str = Field('http://localhost:8081')
    API_VERSION: str
    SWAGGER_PATH: str
    JSON_SWAGGER_PATH: str

    class Config:
        env_prefix = 'PRODUCER_'


class KafkaTopicsSettings(BaseSettings):
    STATUS_ROUTE: str

    class Config:
        env_prefix = 'STORAGE_KAFKA_TOPICS_'


class KafkaSettings(BaseSettings):
    SERVERS: str
    TOPICS: BaseSettings = Field(default_factory=KafkaTopicsSettings)

    class Config:
        env_prefix = 'STORAGE_KAFKA_'


class Config(BaseSettings):
    APP: AppSettings = AppSettings()
    KAFKA: KafkaSettings = KafkaSettings()


CONFIG = Config()
