def detect_cycle(graph):
    visited = dict(zip(graph.vertices,[False] * len(graph.vertices)))
    for i in graph.vertices:
        if dfs_visiting(graph, i, visited):
            return True
    return False


def dfs_visiting(graph, vertex, visited):
    if visited[vertex]:
        return True

    visited[vertex] = True
    current_adj_head = graph.adj_list[vertex].head
    while current_adj_head is not None:
        data = current_adj_head.val
        if dfs_visiting(graph, data, visited):
            return True
        current_adj_head = current_adj_head.next
    visited[vertex] = False
    return False
