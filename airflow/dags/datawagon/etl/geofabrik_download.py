import wget
import os
from loguru import logger

from src.core.config import GEOFABRIK_CONFIG, OSM_CONFIG


def run():
    FILES = OSM_CONFIG.FILES.split(",")
    URLS = GEOFABRIK_CONFIG.URLS.split(",")

    for index, URL in enumerate(URLS):
        if os.path.exists(FILES[index]):
            os.remove(FILES[index])

        wget.download(url=URL, out=FILES[index])
        logger.info(f'[+] Success downloading "{URL}" to "{FILES[index]}"')
