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


class GraphFirstSearch:
    marked: list
    edge_to: list
    root_id: int

    def has_path_to(self, vertex_id: int):
        return self.marked[vertex_id]

    def path_to(self, vertex_id: int):
        if not self.has_path_to(vertex_id):
            return None

        path = []
        while vertex_id != self.root_id:
            path.insert(0, vertex_id)
            vertex_id = self.edge_to[vertex_id]

        path.insert(0, self.root_id)
        return path


class DepthFirstSearch(GraphFirstSearch):
    def __init__(self, graph: Graph, root_id: int):
        self.marked = [False for _ in range(len(graph.vertexes))]
        self.edge_to = [None for _ in range(len(graph.vertexes))]
        self.graph = graph
        self.root_id = root_id

        self.__depth_first_paths(vertex_id=self.root_id)

    def __depth_first_paths(self, vertex_id):
        self.marked[vertex_id] = True

        for adj in self.graph.vertexes[vertex_id].adjacencies:
            if not self.marked[adj]:
                self.__depth_first_paths(adj)
                self.edge_to[adj] = vertex_id


class BreadthFirstSearch(GraphFirstSearch):
    def __init__(self, graph: Graph, root_id: int):
        self.marked = [False for _ in range(len(graph.vertexes))]
        self.edge_to = [None for _ in range(len(graph.vertexes))]
        self.dist_to_root = [None for _ in range(len(graph.vertexes))]
        self.graph = graph
        self.root_id = root_id

        self.__breadth_first_paths(vertex_id=self.root_id)

    def __breadth_first_paths(self, vertex_id):
        search_queue = [vertex_id]
        self.marked[vertex_id] = True
        self.dist_to_root[vertex_id] = 0

        while search_queue:
            proceed_id = search_queue.pop()

            for adj in self.graph.vertexes[proceed_id].adjacencies:
                if not self.marked[adj]:
                    search_queue.insert(0, adj)
                    self.marked[adj] = True
                    self.edge_to[adj] = proceed_id
                    self.dist_to_root[adj] = self.dist_to_root[proceed_id] + 1


def graph_from_data(data: list, graph_type):
    """
    Example of input data: ['13', '0 5', '4 3', '0 1', '9 12', '6 4', '5 4', '0 2']
    :param data: List of strings.
                 First string - number of vertexes in graph.
                 All subsequent strings - pairs of vertexes' ids separated by space to be connected.
    :param graph_type: Undigraph or Digraph object
    :return: Graph object
    """
    g = graph_type(int(data[0]))

    for edge in data[1:]:
        vertexes = [int(v) for v in edge.split(' ')]
        g.add_edge(*vertexes)

    return g
