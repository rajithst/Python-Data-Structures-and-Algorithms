from graph.delete_edge import delete_edge
from graph.graph import Graph
from graph.BFS import graph_bfs_traversal
from graph.DFS import graph_dfs_traversal
from graph.detect_cycle_in_a_directed_graph import detect_cycle
from graph.find_mother_vertex import find_mother_vertex_naive
from graph.find_shortest_path import shortest_path_find
from graph.number_of_edges_of_a_undirected_graph import count_edges
from graph.find_path_exist import bfs_traversal_path_exist, dfs_traversal_path_exist
from graph.undirected_graph_is_a_tree_or_not import is_tree


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


def find_mother_vertex():
    vertices = [0, 1, 2, 3, 4]
    edges = [(0, 1), (2, 3), (3, 0), (3, 4), (4, 2)]

    g1 = Graph(vertices)
    for u, v in edges:
        g1.add_edge(u, v)
    g1.print_graph()
    print(find_mother_vertex_naive(g1))


def find_shortest_path():
    vertices = [0, 1, 2, 3, 4, 5]
    edges = [(0, 1), (0, 2), (0, 3), (2, 4), (3, 5), (5, 4)]

    g1 = Graph(vertices)
    for u, v in edges:
        g1.add_edge(u, v)
    # g1.print_graph()
    print(shortest_path_find(g1, source=0))


def count_edges_of_a_undirected_graph():
    vertices = [0, 1, 2, 3, 4, 5]
    edges = [(0, 1), (0, 2), (0, 3), (2, 4), (3, 5), (5, 4)]

    g1 = Graph(vertices)
    for u, v in edges:
        g1.add_edge(u, v, directed=False)
    print(count_edges(g1))


def path_exist_bfs():
    vertices = [0, 1, 2, 3, 4, 5]
    edges = [(0, 1), (0, 2), (0, 3), (2, 4), (3, 5), (5, 4)]

    g1 = Graph(vertices)
    for u, v in edges:
        g1.add_edge(u, v, directed=True)
    g1.print_graph()
    print(bfs_traversal_path_exist(g1, start=0, destination=5))


def path_exist_dfs():
    vertices = [0, 1, 2, 3, 4, 5]
    edges = [(0, 1), (0, 2), (0, 3), (2, 4), (3, 5), (5, 4)]

    g1 = Graph(vertices)
    for u, v in edges:
        g1.add_edge(u, v, directed=True)
    g1.print_graph()
    print(dfs_traversal_path_exist(g1, start=2, destination=3))


def is_a_tree():
    vertices = [0, 1, 2, 3, 4]
    edges = [(0, 1), (0, 2), (2, 1), (0, 3), (3, 4)]

    g1 = Graph(vertices)
    for u, v in edges:
        g1.add_edge(u, v, directed=False)
    g1.print_graph()
    print(is_tree(g1, start=0))


def remove_edge():
    vertices = [0, 1, 2, 3, 4]
    edges = [(0, 1), (0, 2), (1, 3), (2, 4), (4, 0)]

    g1 = Graph(vertices)
    for u, v in edges:
        g1.add_edge(u, v)
    g1.print_graph()
    print(delete_edge(g1, start=0, end=1))
    g1.print_graph()


remove_edge()
