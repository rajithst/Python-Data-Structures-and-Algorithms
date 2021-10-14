from graph.bipartite_graph import is_bipartite_graph
from graph.clone_undirected_graph import clone_graph
from graph.delete_edge import delete_edge
from graph.graph import Graph
from graph.traversal.BFS import graph_bfs_traversal
from graph.traversal.DFS import graph_dfs_traversal
from graph.detect_cycles_in_a_graph import detect_cycle_directed, detect_cycle_undirected
from graph.find_mother_vertex import find_mother_vertex_naive
from graph.shortest_path.BFS_SSSP import shortest_path_find
from graph.topological_sort.khans_algorithm import topological_sort_bfs
from graph.number_of_edges_of_a_undirected_graph import count_edges
from graph.find_path_exist import bfs_traversal_path_exist, dfs_traversal_path_exist
from graph.topological_sort.topological_sort_dfs import topological_sort_dfs
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


def detect_cycles_directed():
    vertices = [0, 1, 2, 3, ]
    edges = [(0, 1), (1, 2), (1, 3), (3, 2)]

    g1 = Graph(vertices)
    for u, v in edges:
        g1.add_edge(u, v)
    g1.print_graph()
    print(detect_cycle_directed(g1))


def detect_cycles_undirected():
    vertices = [0, 1, 2, 3, 4]
    edges = [(0, 1), (1, 2), (1, 3), (3, 4)]

    g1 = Graph(vertices)
    for u, v in edges:
        g1.add_edge(u, v, directed=False)
    g1.print_graph()
    print(detect_cycle_undirected(g1, start=0))


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


def clone_undirected_graph():
    vertices = [0, 1, 2, 3, 4]
    edges = [(0, 1), (0, 2), (1, 3), (2, 4), (4, 0)]

    g1 = Graph(vertices)
    for u, v in edges:
        g1.add_edge(u, v, directed=False)
    g1.print_graph()
    res = clone_graph(0, g1)
    print(res.neighbours)


def check_bipartite_graph():
    vertices = [1, 2, 3, 4]
    edges = [(1, 2), (2, 3), (3, 4), (4, 1)]

    g1 = Graph(vertices)
    for u, v in edges:
        g1.add_edge(u, v, directed=False)
    g1.print_graph()
    print(is_bipartite_graph(g1))


def khans_algorithm_topological_sort_using_bfs():
    vertices = [0, 1, 2, 3, 4, 5]
    edges = [(1, 2), (0, 2), (2, 4), (2, 3), (4, 5), (3, 5)]

    g1 = Graph(vertices)
    for u, v in edges:
        g1.add_edge(u, v)
    g1.print_graph()
    print(topological_sort_bfs(g1))


def topological_sort_using_dfs():
    vertices = [0, 1, 2, 3, 4, 5]
    edges = [(1, 2), (0, 2), (2, 4), (2, 3), (4, 5), (3, 5)]

    g1 = Graph(vertices)
    for u, v in edges:
        g1.add_edge(u, v)
    g1.print_graph()
    print(topological_sort_dfs(g1))


topological_sort_using_dfs()
