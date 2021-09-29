def cycle_exist(graph, node, visited, parent):
    visited[node] = True

    adjacent = graph.adj_list[node].head
    while adjacent:
        if not visited[adjacent.val]:
            if cycle_exist(graph, adjacent.val, visited, node):
                return False
        elif adjacent.val != parent:
            return True
        adjacent = adjacent.next
    return False


def is_tree(g, start):
    visited = {}
    for v in g.vertices:
        visited[v] = False

    if cycle_exist(g, start, visited, -1):
        return False

    for v in g.vertices:
        if not visited[v]:
            return False
    return True
