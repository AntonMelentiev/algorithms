from copy import copy

from education_part.data_structures import MinPriorityQueue
from education_part.graphs import Vertex, Edge
from education_part.connectivity import QuickUnion


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
    def __init__(self, graph: EdgeWeightedGraph):
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


class LazyPrimMST:
    def __init__(self, graph: EdgeWeightedGraph):
        self.graph = graph
        self.mst = []
        self.marked = [False for _ in range(self.graph.vertexes_number)]
        self.pq = MinPriorityQueue()
        self._visit(self.graph.vertexes[0])

        while (not self.pq.is_empty()) and (len(self.mst) < self.graph.vertexes_number - 1):
            edge = self.pq.pop_min()
            v1 = edge.either_vertex()
            v2 = edge.other_vertex(v1)

            if self.marked[v1.id] and self.marked[v2.id]:
                continue

            self.mst.append(edge)

            if not self.marked[v1.id]:
                self._visit(v1)

            if not self.marked[v2.id]:
                self._visit(v2)

    def _visit(self, vertex):
        self.marked[vertex.id] = True

        for edge in vertex.adjacencies:
            if not self.marked[edge.other_vertex(vertex).id]:
                self.pq.add_to_queue(edge, edge.weight)

    def mst_edges(self):
        return self.mst

    def mst_weight(self):
        weight = 0

        for edge in self.mst_edges():
            weight += edge.weight

        return weight


if __name__ == '__main__':
    from education_part.graphs import edge_weight_graph_from_data

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
    print('-' * 50)
    print(f'Edge weighted graph representation: \n{g}')

    print('-' * 50)
    print('Kruskal Minimum Spain Trees:')
    kruskal_mst = KruskalMST(g)
    print('MST (minimum span tree) for given graph:')
    for edge in kruskal_mst.mst_edges():
        print(edge)
    print(f'\nMST weight: {kruskal_mst.mst_weight()}')

    print('-' * 50)
    print('Lazy Prim Minimum Spain Trees:')

    print('-' * 50)
    print('Kruskal Minimum Spain Trees:')
    prim_mst = LazyPrimMST(g)
    print('MST (minimum span tree) for given graph:')
    for edge in sorted(prim_mst.mst_edges()):
        print(edge)
    print(f'\nMST weight: {prim_mst.mst_weight()}')

    print('-' * 50)
    print('Lazy Prim Minimum Spain Trees:')
