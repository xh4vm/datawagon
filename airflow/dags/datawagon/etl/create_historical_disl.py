from src.extract.excel import ExcelExtractor
from src.core.config import HACKATHON_CONFIG, NODES
from src.load.clickhouse import ClickhouseLoader
from src.transform.disl import DislTransformer


def run():
    extractor = ExcelExtractor(path=HACKATHON_CONFIG.DISL_PATH)

    disl_transformer = DislTransformer()

    disls_df = extractor.extract()

    disls_data = disl_transformer.transform(disls=disls_df)

    loader = ClickhouseLoader(
        host=NODES[2].HOST,
        port=NODES[2].PORT,
        user=NODES[2].USER,
        password=NODES[2].PASSWORD,
        alt_hosts=[f"{NODE.HOST}:{NODE.PORT}" for NODE in NODES],
    )

    loader.load(data=disls_data, table="status_route")
