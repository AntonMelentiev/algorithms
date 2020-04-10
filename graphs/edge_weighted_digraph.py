import math

from data_structures.priority_queue import IndexMinPriorityQueue
from graphs.graph import Vertex, Diedge


class EdgeWeightedDigraph:
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
        v1 = edge.from_vertex()
        v2 = edge.to_vertex()

        if v1 not in self.vertexes:
            raise IndexError(v1.id)
        if v2 not in self.vertexes:
            raise IndexError(v2.id)

        self.edges.append(edge)
        self.edges_number += 1
        v1.adjacencies.append(edge)


class DijkstraShortestPath:
    def __init__(self, graph: EdgeWeightedDigraph, source_vertex: Vertex):
        self.graph = graph
        self.source_vertex = source_vertex
        self.edge_to = [None for _ in range(self.graph.vertexes_number)]
        self.dist_to = [math.inf for _ in range(self.graph.vertexes_number)]
        self.pq = IndexMinPriorityQueue()

        self.dist_to[self.source_vertex.id] = 0
        self.pq.add_to_queue(self.source_vertex, 0)

        while not self.pq.is_empty():
            vertex = self.pq.pop_min()
            for edge in vertex.adjacencies:
                self._relax(edge)

    def shortest_path_to(self, destination_vertex: Vertex):
        if destination_vertex == self.source_vertex:
            return 0, None

        dist = self.dist_to[destination_vertex.id]
        path = [destination_vertex.id]
        edge = self.edge_to[destination_vertex.id]

        while edge.from_vertex() != self.source_vertex:
            path.insert(0, edge.from_vertex().id)
            edge = self.edge_to[edge.from_vertex().id]

        path.insert(0, edge.from_vertex().id)

        return dist, path

    def _relax(self, edge):
        v1 = edge.from_vertex()
        v2 = edge.to_vertex()

        if self.dist_to[v2.id] > self.dist_to[v1.id] + edge.weight:
            self.dist_to[v2.id] = self.dist_to[v1.id] + edge.weight
            self.edge_to[v2.id] = edge

            if v2 in self.pq.items:
                self.pq.update_priority(v2, self.dist_to[v2.id])
            else:
                self.pq.add_to_queue(v2, self.dist_to[v2.id])


if __name__ == '__main__':
    from graphs.graph import edge_weight_digraph_from_data

    g_data = [
        '8',
        '0 1 5.0',
        '0 4 9.0',
        '0 7 8.0',
        '1 2 12.0',
        '1 3 15.0',
        '1 7 4.0',
        '2 3 3.0',
        '2 6 11.0',
        '3 6 9.0',
        '4 5 4.0',
        '4 6 20.0',
        '4 7 5.0',
        '5 2 1.0',
        '5 6 13.0',
        '7 5 6.0',
        '7 2 7.0'
    ]

    g = edge_weight_digraph_from_data(g_data, EdgeWeightedDigraph)
    print('-' * 50)
    print(f'Edge weighted graph representation: \n{g}')

    dsp_from = g.vertexes[0]
    dsp_to = g.vertexes[6]
    dsp = DijkstraShortestPath(g, dsp_from)
    sp_dist, sp_path = dsp.shortest_path_to(dsp_to)
    print(sp_dist)
    print(sp_path)
