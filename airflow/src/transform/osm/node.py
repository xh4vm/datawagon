from typing import Iterator, Any

from src.transform.base import BaseTransformer
from src.models.osm import Node


class NodeTransformer(BaseTransformer):
    def transform(
        self, raw: Iterator[dict[str, Any]], to_dict: bool = False
    ) -> Iterator[Any]:
        for raw_elem in raw:
            elem = Node(**raw_elem)
            yield elem.model_dump() if to_dict else elem
