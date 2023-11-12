from src.models.base import JSONModel


class StationData(JSONModel):
    osm_id: int
    station_id: int
