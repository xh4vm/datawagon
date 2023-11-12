import osmium
import shapely.wkb as wkblib
from loguru import logger


class RailwayHandler(osmium.SimpleHandler):
    relations: list = []
    relation_members: list = []
    ways: list = []
    nodes: list = []

    def __init__(self):
        osmium.SimpleHandler.__init__(self)
        self.wkbfab = osmium.geom.WKBFactory()

    def create_geom(self, geom: type, method: str):
        try:
            wkb = getattr(self.wkbfab, method)(geom)
            geo = wkblib.loads(wkb, hex=True)

        except Exception as exception:
            logger.error(exception)
            logger.error(geom)
            return None

        return geo

    def node(self, n):
        if (
            n.tags.get("railway") == "stop"
            and n.tags.get("train") == "yes"
            and n.tags.get("name") is not None
        ):
            geo = self.create_geom(n, "create_point")

            if geo is None:
                return

            self.nodes.append({"n_id": n.id, "geo": geo, **dict(n.tags)})

    def way(self, w):
        if w.tags.get("railway") == "rail":
            geo = self.create_geom(w, "create_linestring")

            if geo is None:
                return

            self.ways.append({"w_id": w.id, "geo": geo, **dict(w.tags)})

    def relation(self, r):
        if (
            r.tags.get("type") == "route"
            and r.tags.get("route") == "train"
            and r.tags.get("name") is not None
        ):
            self.relations.append({"r_id": r.id, **dict(r.tags)})

            for member in r.members:
                self.relation_members.append(
                    {
                        "r_id": r.id,
                        "ref": member.ref,
                        "role": member.role,
                        "type": member.type,
                    }
                )
