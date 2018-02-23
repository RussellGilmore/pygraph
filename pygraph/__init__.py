from typing import Tuple, Set


def main():
    print("hello world!")


Vertex = Tuple[str, object]
Edge = Set[Vertex]


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def adjacent(self, x: Vertex, y: Vertex) -> bool:
        raise NotImplementedError

    def neigbors(self, v: Vertex) -> [Vertex]:
        raise NotImplementedError

    def add_vertex(self, v: Vertex) -> bool:
        raise NotImplementedError

    def remove_vertex(self, v: Vertex) -> Vertex:
        raise NotImplementedError

    def add_edge(self, e: Edge) -> Edge:
        raise NotImplementedError

    def remove_edge(self, e: Edge) -> Edge:
        raise NotImplementedError
