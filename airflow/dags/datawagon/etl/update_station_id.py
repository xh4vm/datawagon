from src.extract.csv import CSVExtractor
from src.core.config import HACKATHON_CONFIG, POSTGRES_CONFIG
from src.load.postgres import PostgresLoader
from src.transform.station import StationTransformer
from src.schema import SCHEMA


def run():
    extractor = CSVExtractor(path=HACKATHON_CONFIG.PARTIAL_RESULTS_PATH)
    
    station_transformer = StationTransformer()

    stations_df = extractor.extract()

    stations_data = station_transformer.transform(stations_df=stations_df)

    updater = PostgresLoader(
        settings=POSTGRES_CONFIG,
        metadata={},
        schema=SCHEMA,
    )
