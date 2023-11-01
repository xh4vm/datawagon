from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Body

from src.containers.status_route import ServiceContainer
from src.services.producer.kafka import KafkaProducer
from src.core.config import CONFIG

from src.models.status_route import StatusRoute, RouteData


router = APIRouter(prefix='/route', tags=['Routes'])
URL = f'{CONFIG.APP.HOST}:{CONFIG.APP.PORT}{CONFIG.APP.API_PATH}/{CONFIG.APP.API_VERSION}/route/status'


@router.post(path='/status', name='Produce status rail route')
@inject
async def status_route(
    status: RouteData = Body(title='StatusRoute', alias='status_route'),
    kafka_producer: KafkaProducer = Depends(Provide[ServiceContainer.kafka_producer]),
) -> None:

    status = StatusRoute(**status.dict())

    async with kafka_producer as producer:
        await producer.produce(topic=CONFIG.KAFKA.TOPICS.STATUS_ROUTE, key=None, value=status)
