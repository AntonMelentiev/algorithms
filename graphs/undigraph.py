from graphs.graph import Graph, Vertex


class Undigraph(Graph):
    def __init__(self, vertex_num):
        self.vertexes_number = vertex_num
        self.vertexes = [Vertex(v_id) for v_id in range(vertex_num)]
        self.edges_number = 0

    def __repr__(self):
        str_repr = ''

        for vertex in self.vertexes:
            for adjacency in sorted(vertex.adjacencies):
                str_repr += f'{vertex.id} - {adjacency}\n'

        return str_repr

    def add_edge(self, id_1: int, id_2: int):
        if id_1 > self.vertexes_number:
            raise IndexError(id_1)
        if id_2 > self.vertexes_number:
            raise IndexError(id_2)

        self.edges_number += 1
        self.vertexes[id_1].adjacencies.append(id_2)

        if id_1 != id_2:
            self.vertexes[id_2].adjacencies.append(id_1)


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


class ConnectedComponents:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.marked = [False for _ in range(len(graph.vertexes))]
        self.component_id = [None for _ in range(len(graph.vertexes))]
        self.components_count = 0

        self.__connected_components()

    def __connected_components(self):
        for vertex in self.graph.vertexes:
            if not self.marked[vertex.id]:
                self.__depth_first_paths(vertex.id)
                self.components_count += 1

    def __depth_first_paths(self, vertex_id):
        self.marked[vertex_id] = True
        self.component_id[vertex_id] = self.components_count

        for adj in self.graph.vertexes[vertex_id].adjacencies:
            if not self.marked[adj]:
                self.__depth_first_paths(adj)
                self.component_id[adj] = self.components_count

    def components_number(self):
        return self.components_count

    def component_if_for_vertex_id(self, vertex_id: int):
        return self.component_id[vertex_id]


if __name__ == '__main__':
    from graphs.graph import graph_from_data, TypicalGraphProcessing

    # Vertex
    v = Vertex(0)
    print(v)
    print('-' * 55, end='\n\n')

    # Graph
    g = graph_from_data(
        data=['13', '0 5', '4 3', '0 1', '9 12', '6 4', '5 4', '0 2', '11 12', '9 10', '0 6', '7 8', '9 11', '5 3'],
        graph_type=Undigraph,
    )
    # print(g)
    print(f'Vertexes in graph: {g.vertexes_number}')
    print(f'Edges in graph: {g.edges_number}')
    print(f'Max graphs degree: {TypicalGraphProcessing.max_degree(g)}')
    print(f'Average graphs degree: {TypicalGraphProcessing.average_degree(g)}')
    print(f'Number of self loops: {TypicalGraphProcessing.self_loops_number(g)}')
    print(f'Adjacencies of vertex 12: {TypicalGraphProcessing.vertex_adjacencies(g, 12)}')
    print(f'Degree of vertex 12: {TypicalGraphProcessing.vertex_degree(g, 12)}')

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

    # Connected Components
    print('\n--- Connected Components ---')
    cc = ConnectedComponents(g)
    print(f'Number of connected components: {cc.components_number()}')
    print(f'Component id for vertex id 7: {cc.component_if_for_vertex_id(7)}')
    print(f'Components ids: {cc.component_id}')

    print('-'*55, end='\n\n')

    # g2 = graph_from_data(['6', '0 5', '2 4', '2 3', '1 2', '0 1', '3 4', '3 5', '0 2'])
    # # print(g2)
    # start_id_2 = 0
    # print(f'Start id: {start_id_2}')
    # bfs_2 = BreadthFirstSearch(g2, start_id_2)
    # print(bfs_2.marked)
    # print(bfs_2.edge_to)
    # print(bfs_2.dist_to_root)
