from typing import Optional, Type

from dependency_injector import containers, providers

from src.services.extractor.base import BaseExtractor


class ServiceFactory(providers.Factory):
    provided_type: Optional[Type] = BaseExtractor


class BaseContainer(containers.DeclarativeContainer):
    settings = providers.Dependency(instance_of=object)
