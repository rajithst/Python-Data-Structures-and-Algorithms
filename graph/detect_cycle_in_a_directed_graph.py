def detect_cycle_directed(graph):
    visited = dict(zip(graph.vertices, [False] * len(graph.vertices)))
    for i in graph.vertices:
        if dfs_visiting(graph, i, visited):
            return True
    return False


def detect_cycle_undirected(graph,start):
    visited = dict(zip(graph.vertices, [False] * len(graph.vertices)))
    if dfs_visiting_undirected(graph,start, visited, parent=-1):
        return True
    return False


def dfs_visiting_undirected(graph, vertex, visited, parent):
    visited[vertex] = True
    head = graph.adj_list[vertex].head
    while head:
        if not visited[head.val]:
            if dfs_visiting_undirected(graph, head.val, visited, vertex):
                return True
        elif head.val != parent:
            return True
        head = head.next
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

# TODO detect cycles using dfs and stack ds method
