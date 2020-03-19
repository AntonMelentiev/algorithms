from dataclasses import dataclass, field


@dataclass
class Vertex:
    id: int
    adjacencies: list = field(default_factory=list)
    value: object = None


class Graph:
    vertexes_number: int
    vertexes: list
    edges_number: int

    def __repr__(self):
        raise NotImplemented

    def add_edge(self, id_1: int, id_2: int):
        raise NotImplemented


class TypicalGraphProcessing:
    @staticmethod
    def vertex_degree(graph: Graph, v_id: int):
        return len(graph.vertexes[v_id].adjacencies)

    @staticmethod
    def vertex_adjacencies(graph: Graph, v_id: int):
        return graph.vertexes[v_id].adjacencies

    @staticmethod
    def max_degree(graph: Graph):
        max_degree = 0

        for v in graph.vertexes:
            if len(v.adjacencies) > max_degree:
                max_degree = len(v.adjacencies)

        return max_degree

    @staticmethod
    def average_degree(graph: Graph):
        return graph.edges_number / len(graph.vertexes)

    @staticmethod
    def self_loops_number(graph: Graph):
        self_loops_number = 0

        for v in graph.vertexes:
            self_loops_number += v.adjacencies.count(v.id)

        return self_loops_number


def graph_from_data(data: list, graphtype: Graph):
    """
    Example of input data: ['13', '0 5', '4 3', '0 1', '9 12', '6 4', '5 4', '0 2']
    :param data: List of strings.
                 First string - number of vertexes in graph.
                 All subsequent strings - pairs of vertexes' ids separated by space to be connected.
    :param graphtype: Undigraph or Digraph object
    :return: Graph object
    """
    g = graphtype(int(data[0]))

    for edge in data[1:]:
        vertexes = [int(v) for v in edge.split(' ')]
        g.add_edge(*vertexes)

    return g