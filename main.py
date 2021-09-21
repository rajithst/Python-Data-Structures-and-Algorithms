from graph.graph import Graph
from graph.BFS import graph_bfs_traversal
vertices = ["A","B","C","D","E","F","G"]
edges = [("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","E"),("F","G")]
gp = Graph(vertices)
for u,v in edges:
    gp.add_edge(u,v)
gp.print_graph()
graph_bfs_traversal(gp, source="A")
