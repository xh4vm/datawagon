import osmium
import shapely.wkb as wkblib


class RailwayHandler(osmium.SimpleHandler):
    relations: list = []
    relation_members: list = []
    ways: list = []
    nodes: list = []

    def __init__(self):
        osmium.SimpleHandler.__init__(self)
        self.wkbfab = osmium.geom.WKBFactory()

    def node(self, n):
        if n.tags.get("railway") == "stop" and n.tags.get("train") == "yes" and n.tags.get("name") is not None:
            wkb = self.wkbfab.create_point(n)
            geo = wkblib.loads(wkb, hex=True)
            
            self.nodes.append({'n_id': n.id, 'geo': geo, **dict(n.tags)})

    def way(self, w):
        if w.tags.get("railway") is not None and w.tags.get("name") is not None:
            wkb = self.wkbfab.create_linestring(w)
            geo = wkblib.loads(wkb, hex=True)

            self.ways.append({"w_id": w.id, "geo": geo, **dict(w.tags)})

    def relation(self, r):
        if r.tags.get("type") == "route" and (r.tags.get("route") == "train" or r.tags.get("route") == "railway") and r.tags.get("name") is not None:

            self.relations.append({"r_id": r.id, **dict(r.tags)})

            for member in r.members:
                self.relation_members.append({
                    "r_id": r.id, 
                    "ref": member.ref, 
                    "role": member.role, 
                    "type": member.type,
                })
