from graphs.graph import Vertex, Diedge


class EdgeWeightedDiraph:
    def __init__(self, vertex_num):
        self.vertexes_number = vertex_num
        self.vertexes = [Vertex(v_id) for v_id in range(vertex_num)]
        self.edges_number = 0
        self.edges = []

    def __repr__(self):
        str_repr = ''

        for edge in sorted(self.edges):
            str_repr += str(edge) + '\n'

        return str_repr

    def add_edge(self, edge: Diedge):
        v1 = edge.either_vertex()
        v2 = edge.other_vertex(v1)

        if v1 not in self.vertexes:
            raise IndexError(v1.id)
        if v2 not in self.vertexes:
            raise IndexError(v2.id)

        self.edges.append(edge)
        self.edges_number += 1
        v1.adjacencies.append(edge)
