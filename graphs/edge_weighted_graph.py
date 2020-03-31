from copy import copy

from graphs.graph import Vertex, Edge
from connectivity.connectivity import QuickUnion


class EdgeWeightedGraph:
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

    def add_edge(self, edge: Edge):
        v1 = edge.either_vertex()
        v2 = edge.other_vertex(v1)

        if v1 not in self.vertexes:
            raise IndexError(v1.id)
        if v2 not in self.vertexes:
            raise IndexError(v2.id)

        self.edges.append(edge)
        self.edges_number += 1
        v1.adjacencies.append(edge)

        if v1 != v2:
            v2.adjacencies.append(edge)


class KruskalMST:
    def __init__(self, graph):
        self.graph = graph
        self.quick_union = QuickUnion(self.graph.vertexes_number)
        self.edges = sorted(copy(self.graph.edges), reverse=True)
        self.mst = []

        while len(self.mst) < self.graph.vertexes_number - 1:
            edge = self.edges.pop()
            v1 = edge.either_vertex()
            v2 = edge.other_vertex(v1)

            if not self.quick_union.is_connected(v1.id, v2.id):
                self.mst.append(edge)
                self.quick_union.union(v1.id, v2.id)

    def mst_edges(self):
        return self.mst

    def mst_weight(self):
        weight = 0

        for edge in self.mst_edges():
            weight += edge.weight

        return weight


if __name__ == '__main__':
    from graphs.graph import edge_weight_graph_from_data

    v1 = Vertex(id=1)
    v2 = Vertex(id=2)
    v3 = Vertex(id=3)
    e1 = Edge(v1, v2, 5)
    e2 = Edge(v1, v3, 10)
    print(e1)
    print(e2)
    print(e1 < e2)

    g_data = [
        '8',
        '0 7 0.16',
        '2 3 0.17',
        '1 7 0.19',
        '0 2 0.26',
        '5 7 0.28',
        '1 3 0.29',
        '1 5 0.32',
        '2 7 0.34',
        '4 5 0.35',
        '1 2 0.36',
        '4 7 0.37',
        '0 4 0.38',
        '6 2 0.40',
        '3 6 0.52',
        '6 0 0.58',
        '6 4 0.93',
    ]

    g = edge_weight_graph_from_data(g_data, EdgeWeightedGraph)
    print(g)

    kruskal_mst = KruskalMST(g)

    for edge in kruskal_mst.mst_edges():
        print(edge)

    print(kruskal_mst.mst_weight())
