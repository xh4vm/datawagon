from loguru import logger

from src.extract.osm_pbf import OSMPBFExtractor
from src.core.config import OSM_CONFIG, POSTGRES_CONFIG
from src.utils.osm.handlers.railway import RailwayHandler
from src.load.postgres import PostgresLoader
from src.schema import SCHEMA, Schema
from src.transform.osm.railway import RailwayTransformer, Railway
from src.transform.osm.node import NodeTransformer, Node


def run():
    handler = RailwayHandler()
    extractor = OSMPBFExtractor(handler=handler, osm_config=OSM_CONFIG)
    railway_transformer = RailwayTransformer()

    nodes, ways, relation_members, relations = extractor.extract()

    data = railway_transformer.transform(ways=ways, members=relation_members, relations=relations)

    loader = PostgresLoader(
        settings=POSTGRES_CONFIG,
        metadata={
            Schema.NODES: Node,
            Schema.RAILWAYS: Railway,
        },
        schema=SCHEMA,
    )

    with loader:
        loader.load(data)
