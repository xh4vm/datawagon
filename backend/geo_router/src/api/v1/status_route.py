from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
import geopandas as gpd
import orjson
from shapely import MultiPoint, to_geojson

from src.containers.producer.kafka import (
    ServiceContainer as KafkaProducerServiceContainer,
)
from src.containers.extractor.clickhouse_postgres import (
    ServiceContainer as ClickhousePostgresServiceContainer,
)
from src.services.producer.kafka import KafkaProducer
from src.services.extractor.clickhouse import ClickhouseExtractor
from src.services.extractor.postgres import PostgresExtractor
from src.models.geo import GeoPointOperdate
from src.core.config import CONFIG

from src.models.status_route import StatusRoute, RouteData
from src.models.train import TrainData, WagonData


router = APIRouter(prefix="/railway", tags=["Railway route API"])


@router.post(path="/status", name="Обработка статуса маршрута поезда")
@inject
async def status_route(
    status: RouteData,
    kafka_producer: KafkaProducer = Depends(
        Provide[KafkaProducerServiceContainer.kafka_producer]
    ),
) -> None:
    status = StatusRoute(**status.model_dump())

    async with kafka_producer as producer:
        await producer.produce(
            topic=CONFIG.KAFKA.TOPICS.STATUS_ROUTE, key=None, value=status
        )


@router.get(path="/status", name="Получение информации об активных поездах")
@inject
async def map_status_route(
    x1: float,
    x2: float,
    y1: float,
    y2: float,
    ch_extractor: ClickhouseExtractor = Depends(
        Provide[ClickhousePostgresServiceContainer.clickhouse_service]
    ),
    pg_extractor: PostgresExtractor = Depends(
        Provide[ClickhousePostgresServiceContainer.postgres_service]
    ),
) -> dict[str, TrainData]:
    with pg_extractor:
        railways_df = pg_extractor.extract(
            (
                "SELECT * from content.railways "
                "WHERE ST_Intersects( "
                f"ST_MakeEnvelope({min(x1, x2)}, {min(y1, y2)}, {max(x1, x2)}, {max(y1, y2)}, 4326), "
                f"geo)"
            )
        )

        railways_df["geo"] = gpd.GeoSeries.from_wkb(railways_df["geo"])
        railways_gdf = gpd.GeoDataFrame(railways_df, geometry="geo")

        station_df = pg_extractor.extract(
            (
                f"SELECT station_id, location from content.nodes WHERE ST_Contains( "
                f"ST_MakeEnvelope({min(x1, x2)}, {min(y1, y2)}, {max(x1, x2)}, {max(y1, y2)}, 4326), "
                f"location)"
            )
        )

        station_df["location"] = gpd.GeoSeries.from_wkb(station_df["location"])
        station_gdf = gpd.GeoDataFrame(station_df, geometry="location")

    visible_station = (
        station_df["station_id"]
        .dropna()
        .astype("int")
        .astype("string")
        .unique()
        .tolist()
    )

    if len(visible_station) == 0:
        return {}

    join_str = ", ".join(visible_station)

    status_route_df = ch_extractor.extract(
        (
            "SELECT wagnum, train_index, train_st_start, train_st_end, train_st_num, groupArray(st_id_disl) as disl_ids, groupArray(map('operdate', toString(operdate), 'st_id_disl', toString(st_id_disl))) as disls, st_id_dest FROM default.status_route WHERE "
            f"train_st_start IN ({join_str}) OR "
            f"train_st_end IN ({join_str}) OR "
            f"st_id_disl IN ({join_str}) OR "
            f"st_id_dest IN ({join_str}) "
            f"GROUP BY train_index, train_st_start, train_st_end, train_st_num, wagnum, st_id_dest"
        )
    )

    result = {}
    for _, status_route in status_route_df.iterrows():
        locations = station_gdf[
            station_gdf.station_id.isin(
                [
                    *[status_route["disl_ids"]],
                    status_route["st_id_dest"],
                    status_route["train_st_start"],
                    status_route["train_st_end"],
                ]
            )
        ].location.tolist()

        multipoint = MultiPoint(locations)

        railway_df = railways_gdf[railways_gdf.contains(multipoint)]

        if railway_df.size == 0:
            continue

        railway = railway_df.iloc[0].to_dict()
        railway["geo"] = to_geojson(railway["geo"])

        disls = {
            disl["st_id_disl"]: station_gdf[
                station_gdf.station_id == int(disl["st_id_disl"])
            ]
            .iloc[0]
            .to_dict()
            for disl in status_route["disls"]
            if station_gdf[station_gdf.station_id == int(disl["st_id_disl"])].size > 0
        }

        wagon = WagonData(
            number=status_route.wagnum,
            disls=[
                GeoPointOperdate(
                    operdate=disl["operdate"],
                    title=disls[disl["st_id_disl"]].get("title"),
                    geo=orjson.loads(
                        to_geojson(disls[disl["st_id_disl"]].get("location"))
                    ),
                )
                for disl in status_route["disls"]
                if disl["st_id_disl"] in disls
            ],
        )

        if status_route.train_index in result:
            result[status_route.train_index].wagon_counts += 1
            result[status_route.train_index].wagons.append(wagon)

        else:
            result[status_route.train_index] = TrainData(
                wagon_counts=1,
                train_index=status_route.train_index,
                wagons=[wagon],
                railway=orjson.loads(railway.get("geo")),
            )

    return result
