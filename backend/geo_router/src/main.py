from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.middleware import Middleware
from starlette_context import plugins
from dependency_injector import providers
from starlette_context.middleware import RawContextMiddleware

from .resources.json_serializer import JSONSerializerResource
from .resources.string_serializer import StringSerializerResource

from .containers.extractor.clickhouse_postgres import (
    ServiceContainer as ClickhousePostgresServiceContainer,
)
from .containers.producer.kafka import ServiceContainer as KafkaProducerServiceContainer

from .api.v1.status_route import router as status_route_router
from .core.config import CONFIG


def register_di_containers():
    status_route_value_serializer = providers.Resource(
        JSONSerializerResource,
        to_dict=lambda obj: obj.model_dump(),
    )
    status_route_key_serializer = providers.Resource(
        StringSerializerResource, codec="utf-8"
    )

    KafkaProducerServiceContainer(
        key_serializer=status_route_key_serializer,
        value_serializer=status_route_value_serializer,
    )

    ClickhousePostgresServiceContainer()


def register_routers(app: FastAPI):
    API_PATH = f"{CONFIG.APP.API_PATH}/{CONFIG.APP.API_VERSION}"

    app.include_router(router=status_route_router, prefix=API_PATH)


def create_app():
    middleware = [
        Middleware(
            RawContextMiddleware,
            plugins=(plugins.RequestIdPlugin(), plugins.CorrelationIdPlugin()),
        )
    ]

    app = FastAPI(
        title=CONFIG.APP.PROJECT_NAME,
        # docs_url=f'{CONFIG.APP.API_PATH}{CONFIG.APP.SWAGGER_PATH}',
        redoc_url=f"{CONFIG.APP.API_PATH}/redoc",
        openapi_url=f"{CONFIG.APP.API_PATH}{CONFIG.APP.JSON_SWAGGER_PATH}",
        default_response_class=ORJSONResponse,
        middleware=middleware,
    )

    register_routers(app=app)
    register_di_containers()

    return app


app = create_app()
