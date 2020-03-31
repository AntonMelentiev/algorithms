from graphs.graph import Vertex, Edge


class EdgeWeightedGraph:
    def __init__(self, vertex_num):
        self.vertexes_number = vertex_num
        self.vertexes = [Vertex(v_id) for v_id in range(vertex_num)]
        self.edges_number = 0

    def __repr__(self):
        str_repr = ''

        for vertex in self.vertexes:
            for adjacency in sorted(vertex.adjacencies):
                str_repr += f'{vertex.id} --({adjacency.weight})--> {adjacency.other_vertex(vertex).id}\n'

        return str_repr

    def add_edge(self, edge: Edge):
        v1 = edge.either_vertex()
        v2 = edge.other_vertex(v1)

        if v1 not in self.vertexes:
            raise IndexError(v1.id)
        if v2 not in self.vertexes:
            raise IndexError(v2.id)

        self.edges_number += 1
        v1.adjacencies.append(edge)

        if v1 != v2:
            v2.adjacencies.append(edge)


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

    g_data = ['13', '0 5 0.37', '4 3 1.2', '0 1 0.5', '9 12 1', '6 4 0.12', '5 4 0.12', '0 2 0.75']
    g = edge_weight_graph_from_data(g_data, EdgeWeightedGraph)
    print(g)
