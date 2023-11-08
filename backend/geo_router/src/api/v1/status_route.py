from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from typing import Any

from src.containers.status_route import ServiceContainer
from src.services.producer.kafka import KafkaProducer
from src.core.config import CONFIG

from src.models.status_route import StatusRoute, RouteData
from src.models.train import TrainData


router = APIRouter(prefix='/railway', tags=['Railway route API'])


@router.post(path='/status', name='Обработка статуса маршрута поезда')
@inject
async def status_route(
    status: RouteData,
    kafka_producer: KafkaProducer = Depends(Provide[ServiceContainer.kafka_producer]),
) -> None:

    status = StatusRoute(**status.model_dump())

    async with kafka_producer as producer:
        await producer.produce(topic=CONFIG.KAFKA.TOPICS.STATUS_ROUTE, key=None, value=status)


@router.get(path='/status', name='Получение информации об активных поездах')
@inject
async def map_status_route(

) -> list[TrainData]:
    pass
