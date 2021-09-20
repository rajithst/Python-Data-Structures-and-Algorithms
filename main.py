from graph.graph import Graph

g = Graph(4)
g.add_edge(0, 2)
g.add_edge(0, 1)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.print_graph()