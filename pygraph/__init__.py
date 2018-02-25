from typing import Tuple, Set

Vertex = Tuple[str, object]
Edge = Set[Vertex]

def main():
    potato = Graph()
    potato.add_vertex(('A', 'Potato'))
    potato.add_vertex(('B', 'Chicken'))
    # print(potato.all_vertices())
    # potato.remove_vertex(('A', 'Potato'))
    # print(potato.all_vertices())
    v1 = ('A', 'Potato')
    v2 = ('B', 'Chicken')
    v3 = ('C', 'Chocolate')
    print(potato.add_edge((v1, v2)))
    print(potato.add_edge((v1, v3)))

    print(potato.adjacent(v1, v2))
    print(potato.adjacent(v1, v3))

    print(potato.neigbors(v1))

class Graph:
    def __init__(self):
        self.vertices=[]
        self.edges=[]

    def add_vertex(self, v: Vertex) -> bool:
        if v not in self.vertices:
            self.vertices.append(v)
            return True
        else:
            return False

    def remove_vertex(self, v: Vertex) -> Vertex:
        if v in self.vertices:
            temp=v
            self.vertices.remove(v)
            return temp
        else:
            return None

    # Gives all vertices
    def all_vertices(self) -> [Vertex]:
        return self.vertices

    def add_edge(self, e: Edge) -> Edge:
        for v in e:
            if not v in self.vertices:
                return None

        self.edges.append(e)
        return e

    def remove_edge(self, e: Edge) -> Edge:
        return self.edges.remove(e)
        
    def adjacent(self, x: Vertex, y: Vertex) -> bool:
        for e in self.edges:
            if x in e and y in e:
                return True

        return False

    def neigbors(self, v: Vertex) -> [Vertex]:
        # neighbor = []
        s=set()
        # s.add(v)
        for e in self.edges:
            [v1, v2]=e
            if (self.adjacent(v1, v2)):
                s.add(v1)
                s.add(v2)

            s.remove(v)

        return list(s)
