from dependency_injector import containers

from src.services.extractor.clickhouse import ClickhouseExtractor
from src.services.extractor.postgres import PostgresExtractor
from .base import BaseContainer, ServiceFactory


class ServiceContainer(BaseContainer):
    wiring_config = containers.WiringConfiguration(modules=["...api.v1.status_route"])

    clickhouse_service = ServiceFactory(ClickhouseExtractor)

    postgres_service = ServiceFactory(PostgresExtractor)
