from graph.graph import Graph
from graph.BFS import graph_bfs_traversal
from graph.DFS import graph_dfs_traversal
from graph.detect_cycle_in_a_directed_graph import detect_cycle


def bfs_dfs_traversal():
    vertices = ["A", "B", "C", "D", "E", "F", "G"]
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E"), ("F", "G")]
    gp = Graph(vertices)
    for u, v in edges:
        gp.add_edge(u, v)
    gp.print_graph()
    graph_bfs_traversal(gp, source="A")
    graph_dfs_traversal(gp, source="A")


def detect_cycles():
    vertices = [0, 1, 2, 3, ]
    edges = [(0, 1), (1, 2), (1, 3), (3, 2)]

    g1 = Graph(vertices)
    for u, v in edges:
        g1.add_edge(u, v)
    g1.print_graph()
    print(detect_cycle(g1))
