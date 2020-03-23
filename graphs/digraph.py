from graphs.graph import Graph, Vertex


class Digraph(Graph):
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


class TopologicalSort:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.marked = [False for _ in range(len(graph.vertexes))]
        self.path = []

        for vertex in self.graph.vertexes:
            if not self.marked[vertex.id]:
                self.__depth_first_paths(vertex_id=vertex.id)

    def __depth_first_paths(self, vertex_id):
        self.marked[vertex_id] = True

        for adj in self.graph.vertexes[vertex_id].adjacencies:
            if not self.marked[adj]:
                self.__depth_first_paths(adj)

        self.path.append(vertex_id)


class CycleDetector:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.marked = [False for _ in range(len(graph.vertexes))]
        self.path = []
        self.cycle = False
        self.stop = False
        self.cycle_path = []

        for vertex in self.graph.vertexes:
            if not self.marked[vertex.id] and not self.stop:
                self.__depth_first_paths(vertex_id=vertex.id)

    def __depth_first_paths(self, vertex_id):
        self.marked[vertex_id] = True
        self.path.append(vertex_id)

        for adj in self.graph.vertexes[vertex_id].adjacencies:
            if self.stop:
                break

            if not self.marked[adj]:
                self.__depth_first_paths(adj)
            else:
                if adj in self.path:
                    self.cycle = True
                    self.stop = True
                    self.cycle_path = self.path[self.path.index(adj):] + [adj]

        if not self.stop:
            self.path.pop()

    def get_cycle(self):
        if not self.cycle:
            return


if __name__ == '__main__':
    from graphs.graph import graph_from_data, TypicalGraphProcessing, DepthFirstSearch, BreadthFirstSearch

    # Vertex
    v = Vertex(0)
    print(v)
    print('-' * 55, end='\n\n')

    # Graph
    g = graph_from_data(
        data=['13', '0 5', '4 3', '0 1', '9 12', '6 4', '5 4', '0 2', '11 12', '9 10', '0 6', '7 8', '9 11', '3 5'],
        graph_type=Digraph,
    )
    print(g)
    print(f'Vertexes in graph: {g.vertexes_number}')
    print(f'Edges in graph: {g.edges_number}')
    print(f'Max graphs degree: {TypicalGraphProcessing.max_degree(g)}')
    print(f'Average graphs degree: {TypicalGraphProcessing.average_degree(g)}')
    print(f'Number of self loops: {TypicalGraphProcessing.self_loops_number(g)}')
    print(f'Adjacencies of vertex 12: {TypicalGraphProcessing.vertex_adjacencies(g, 12)}')
    print(f'Degree of vertex 12: {TypicalGraphProcessing.vertex_degree(g, 12)}')
    print(f'Adjacencies of vertex 5: {TypicalGraphProcessing.vertex_adjacencies(g, 5)}')
    print(f'Degree of vertex 5: {TypicalGraphProcessing.vertex_degree(g, 5)}')

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

    # Topological sort
    print('\n--- Topological sort ---')
    g2 = graph_from_data(
        data=[7,  '0 5', '0 2', '0 1', '3 6', '3 5', '3 4', '5 2', '6 4', '6 0', '3 2', '1 4'],
        graph_type=Digraph,
    )
    ts = TopologicalSort(g2)
    print(f'Topological sort in given graph: {ts.path}')

    # Cycle Detector
    print('\n--- Cycle Detector ---')
    test_edge = '2 3'  # with cycle
    # test_edge = '3 2'  # without cycle

    g3 = graph_from_data(
        data=[7,  '0 5', '0 2', '0 1', '3 6', '3 5', '3 4', '5 2', '6 4', '6 0', test_edge, '1 4'],
        graph_type=Digraph,
    )
    cd = CycleDetector(g3)
    print(g3)
    print(f'First founded cycle in graph: {cd.cycle_path}')
