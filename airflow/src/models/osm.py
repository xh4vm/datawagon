from .base import JSONModel, UUIDModelMixin, TimeStampedModelMixin


class NodeData(JSONModel, UUIDModelMixin, TimeStampedModelMixin):
    osm_id: int
    st_id: int
    title: str
    location: str
    role: str


class RailwayData(JSONModel, UUIDModelMixin, TimeStampedModelMixin):
    osm_id: int
    title: str
    geo: str
    title_from: str | None
    title_to: str | None
    operator: str | None
    network: str | None


class RailwayNodeData(JSONModel, UUIDModelMixin, TimeStampedModelMixin):
    node_osm_id: int
    railway_osm_id: int | None
