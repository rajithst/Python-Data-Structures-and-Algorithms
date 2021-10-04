def dfs_helper(graph, node, visited, order):
    visited[node] = True
    nei = graph.adj_list[node].head
    while nei:
        if not visited[nei.val]:
            dfs_helper(graph, nei.val, visited, order)
        nei = nei.next
    order.append(node)
    return


def topological_sort_dfs(graph):
    visited = {}
    for i in graph.vertices:
        visited[i] = False
    order = []
    for v in graph.vertices:
        if not visited[v]:
            dfs_helper(graph, v, visited, order)
    order = reversed(order)
    result = " => ".join(list(map(str, order)))
    return result
