from dataclasses import dataclass, field


@dataclass
class Vertex:
    id: int
    adjencies: list = field(default_factory=list)
    value: object = None


def graph_from_data(data: list):
    """
    Example of input data: ['13', '0 5', '4 3', '0 1', '9 12', '6 4', '5 4', '0 2']
    :param data: List of strings.
                 First string - number of vertexes in graph.
                 All subsequent strings - pairs of vertexes' ids separated by space to be connected.
    :return: Graph object
    """
    g = Graph(int(data[0]))

    for edge in data[1:]:
        vertexes = [int(v) for v in edge.split(' ')]
        g.add_edge(*vertexes)

    return g


class Graph:
    def __init__(self, vertex_num):
        self.vertexes_number = vertex_num
        self.vertexes = [Vertex(v_id) for v_id in range(vertex_num)]
        self.edges_number = 0

    def __repr__(self):
        str_repr = ''

        for vertex in self.vertexes:
            for edge in sorted(vertex.adjencies):
                str_repr += f'{vertex.id} - {edge}\n'

        return str_repr

    def add_edge(self, id_1: int, id_2: int):
        if id_1 > self.vertexes_number:
            raise IndexError(id_1)
        if id_2 > self.vertexes_number:
            raise IndexError(id_2)

        self.edges_number += 1
        self.vertexes[id_1].adjencies.append(id_2)

        if id_1 != id_2:
            self.vertexes[id_2].adjencies.append(id_1)


class TypicalGraphProcessing:
    @staticmethod
    def vertex_degree(graph: Graph, v_id: int):
        return len(graph.vertexes[v_id].adjencies)

    @staticmethod
    def vertex_adjacencies(graph: Graph, v_id: int):
        return graph.vertexes[v_id].adjencies

    @staticmethod
    def max_degree(graph: Graph):
        max_degree = 0

        for v in graph.vertexes:
            if len(v.adjencies) > max_degree:
                max_degree = len(v.adjencies)

        return max_degree

    @staticmethod
    def average_degree(graph: Graph):
        return graph.edges_number / len(graph.vertexes)

    @staticmethod
    def self_loops_number(graph: Graph):
        self_loops_number = 0

        for v in graph.vertexes:
            self_loops_number += v.adjencies.count(v.id)

        return self_loops_number


class GraphFirstSearch:
    marked: list
    edge_to: list
    root_id: int

    def has_path_to(self, id: int):
        return self.marked[id]

    def path_to(self, id: int):
        if not self.has_path_to(id):
            return None

        path = []
        while id != self.root_id:
            path.insert(0, id)
            id = self.edge_to[id]

        path.insert(0, self.root_id)
        return path


class DepthFirstSearch(GraphFirstSearch):
    def __init__(self, graph: Graph, root_id: int):
        self.marked = [False for _ in range(len(graph.vertexes))]
        self.edge_to = [None for _ in range(len(graph.vertexes))]
        self.graph = graph
        self.root_id = root_id

        self.__depth_first_pathes(id=self.root_id)

    def __depth_first_pathes(self, id):
        self.marked[id] = True

        for adj in self.graph.vertexes[id].adjencies:
            if not self.marked[adj]:
                self.__depth_first_pathes(adj)
                self.edge_to[adj] = id


class BreadthFirstSearch(GraphFirstSearch):
    def __init__(self, graph: Graph, root_id: int):
        self.marked = [False for _ in range(len(graph.vertexes))]
        self.edge_to = [None for _ in range(len(graph.vertexes))]
        self.dist_to_root = [None for _ in range(len(graph.vertexes))]
        self.graph = graph
        self.root_id = root_id

        self.__breadth_first_paths(id=self.root_id)

    def __breadth_first_paths(self, id):
        search_queue = [id]
        self.marked[id] = True
        self.dist_to_root[id] = 0

        while search_queue:
            proceed_id = search_queue.pop()

            for adj in self.graph.vertexes[proceed_id].adjencies:
                if not self.marked[adj]:
                    search_queue.insert(0, adj)
                    self.marked[adj] = True
                    self.edge_to[adj] = proceed_id
                    self.dist_to_root[adj] = self.dist_to_root[proceed_id] + 1


if __name__ == '__main__':
    # Vertex
    v = Vertex(0)
    print(v)
    print('-' * 55, end='\n\n')

    # Graph
    g = graph_from_data(['13', '0 5', '4 3', '0 1', '9 12', '6 4', '5 4', '0 2', '11 12', '9 10', '0 6', '7 8', '9 11', '5 3'])
    # print(g)
    print(f'Vertexes in graph: {g.vertexes_number}')
    print(f'Edges in graph: {g.edges_number}')
    print(f'Max graphs degree: {TypicalGraphProcessing.max_degree(g)}')
    print(f'Average graphs degree: {TypicalGraphProcessing.average_degree(g)}')
    print(f'Number of self loops: {TypicalGraphProcessing.self_loops_number(g)}')
    print(f'Adjacencies of vertex 1: {TypicalGraphProcessing.vertex_adjacencies(g, 1)}')
    print(f'Degree of vertex 1: {TypicalGraphProcessing.vertex_degree(g, 1)}')

    try:
        g.add_edge(1, 15)
    except IndexError as e:
        print(f'IndexError occurs on index "{e}"')

    # Depth First Search
    print('\n--- Depth First Search ---')
    start_id = 0
    dfs = DepthFirstSearch(g, start_id)
    print(f'Visited vertexes: {dfs.marked}')
    # print(dfs.edge_to)
    print(f'Path from start_id "{start_id}" to id 3: {dfs.path_to(3)}')
    print(f'Path from start_id "{start_id}" to id 6: {dfs.path_to(6)}')
    print(f'Path from start_id "{start_id}" to id 7: {dfs.path_to(7)}')

    # Breadth First Search
    print('\n--- Breadth First Search ---')
    bfs = BreadthFirstSearch(g, start_id)
    print(f'Visited vertexes: {bfs.marked}')
    # print(bfs.edge_to)
    # print(bfs.dist_to_root)
    print(f'Path from start_id "{start_id}" to id 3: {bfs.path_to(3)}')
    print(f'Path from start_id "{start_id}" to id 6: {bfs.path_to(6)}')
    print(f'Path from start_id "{start_id}" to id 7: {bfs.path_to(7)}')

    print('-'*55, end='\n\n')

    g2 = graph_from_data(['6', '0 5', '2 4', '2 3', '1 2', '0 1', '3 4', '3 5', '0 2'])
    # print(g2)
    start_id_2 = 0
    print(f'Start id: {start_id_2}')
    bfs_2 = BreadthFirstSearch(g2, start_id_2)
    print(bfs_2.marked)
    print(bfs_2.edge_to)
    print(bfs_2.dist_to_root)