from dataclasses import dataclass, field


@dataclass
class Vertex:
    id: int
    adjacencies: list = field(default_factory=list)
    value: object = None


class Digraph:
    def __init__(self, vertex_num):
        self.vertexes_number = vertex_num
        self.vertexes = [Vertex(v_id) for v_id in range(vertex_num)]
        self.edges_number = 0

    def __repr__(self):
        str_repr = ''

        for vertex in self.vertexes:
            for adjacency in sorted(vertex.adjacencies):
                str_repr += f'{vertex.id} -> {adjacency}\n'

        return str_repr

    def add_edge(self, id_1: int, id_2: int):
        if id_1 > self.vertexes_number:
            raise IndexError(id_1)
        if id_2 > self.vertexes_number:
            raise IndexError(id_2)

        self.edges_number += 1
        self.vertexes[id_1].adjacencies.append(id_2)
