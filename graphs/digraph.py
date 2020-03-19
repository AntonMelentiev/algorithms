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


if __name__ == '__main__':
    from graphs.graph import graph_from_data, TypicalGraphProcessing

    # Vertex
    v = Vertex(0)
    print(v)
    print('-' * 55, end='\n\n')

    # Graph
    g = graph_from_data(
        data=['13', '0 5', '4 3', '0 1', '9 12', '6 4', '5 4', '0 2', '11 12', '9 10', '0 6', '7 8', '9 11', '5 3'],
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
