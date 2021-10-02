def dfs_helper(graph, start, parent, color, visited):
    visited[start] = color
    head = graph.adj_list[start].head
    while head:
        if visited[head.val] == 0:
            sub_results = dfs_helper(graph, head.val, start, 3 - color, visited)
            if not sub_results:
                return False
        elif head.val != parent and color == visited[head.val]:
            return False
        head = head.next
    return True


def is_bipartite_graph(graph):
    visited = {}
    for v in graph.vertices:
        visited[v] = 0
    start = 1
    parent = -1
    color = 1
    return dfs_helper(graph, start, parent, color, visited)
