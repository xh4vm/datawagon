import os
from src.extract.osm_pbf import OSMPBFExtractor
from src.core.config import OSM_CONFIG, POSTGRES_CONFIG, HACKATHON_CONFIG
from src.utils.osm.handlers.railway import RailwayHandler
from src.load.postgres import PostgresLoader
from src.schema import SCHEMA, Schema
from src.transform.osm.railway import RailwayTransformer, RailwayData
from src.transform.osm.railway_node import RailwayNodeTransformer, RailwayNodeData
from src.transform.osm.node import NodeTransformer, NodeData


def run():
    FILES = OSM_CONFIG.FILES.split(",")

    node_transformer = NodeTransformer()
    railway_transformer = RailwayTransformer()
    railway_node_transformer = RailwayNodeTransformer()

    loader = PostgresLoader(
        settings=POSTGRES_CONFIG,
        metadata={
            Schema.NODES: NodeData,
            Schema.RAILWAYS: RailwayData,
            Schema.RAILWAY_NODES: RailwayNodeData,
        },
        schema=SCHEMA,
    )

    for FILE in FILES:
        handler = RailwayHandler()
        extractor = OSMPBFExtractor(
            handler=handler,
            osm_file=FILE,
            csv_file_path=HACKATHON_CONFIG.PARTIAL_RESULTS_PATH,
        )

        nodes, ways, relation_members, relations = extractor.extract()

        node_data = node_transformer.transform(nodes=nodes)
        railway_data = railway_transformer.transform(
            ways=ways, members=relation_members, relations=relations
        )
        railway_node_data = railway_node_transformer.transform(members=relation_members)

        with loader:
            loader.load(
                {
                    Schema.NODES: node_data,
                    Schema.RAILWAYS: railway_data,
                    Schema.RAILWAY_NODES: railway_node_data,
                },
                truncate_before=True,
            )
