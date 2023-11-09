import wget
import os
from loguru import logger

from src.core.config import GEOFABRIK_CONFIG, OSM_CONFIG


def run():
    if os.path.exists(OSM_CONFIG.FILE):
        os.rename(OSM_CONFIG.FILE, OSM_CONFIG.BACKUP_FILE)

    wget.download(url=GEOFABRIK_CONFIG.URL, out=OSM_CONFIG.FILE)
    logger.info(f'[+] Success downloading "{GEOFABRIK_CONFIG.URL}" to "{OSM_CONFIG.FILE}"')
