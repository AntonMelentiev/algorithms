import math

from data_structures.priority_queue import MinPriorityQueue
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
    def __init__(self, graph: EdgeWeightedDiraph, source_vertex: Vertex):
        self.graph = graph
        self.source_vertex = source_vertex
        self.edge_to = [None for _ in self.graph.vertexes_number]
        self.dist_to = [math.inf for _ in self.graph.vertexes_number]
        self.pq = MinPriorityQueue()

        self.dist_to[self.source_vertex.id] = 0
        self.pq.add_to_queue(self.source_vertex, 0)

        while not self.pq.is_empty():
            vertex = self.pq.pop_min()
            for edge in vertex.adjacencies:
                self._relax(edge)

    def _relax(self, edge):
        v1 = edge.from_vertex()
        v2 = edge.to_vertex()

        if self.dist_to[v2] > self.dist_to[v1.id] + edge.weight:
            self.dist_to[v2] = self.dist_to[v1.id] + edge.weight
            self.edge_to[v2.id] = edge

            if v2 in self.pq.items:
                self.pq.decrease_key(v2, self.dist_to[v2.id])
            else:
                self.pq.add_to_queue(v2, self.dist_to[v2.id])
