import wget
from loguru import logger

from src.core.config import GEOFABRIK_CONFIG, OSM_CONFIG


def run():
    wget.download(url=GEOFABRIK_CONFIG.URL, out=OSM_CONFIG.FILE)
    logger.info(f'[+] Success downloading "{GEOFABRIK_CONFIG.URL}" to "{OSM_CONFIG.FILE}"')
