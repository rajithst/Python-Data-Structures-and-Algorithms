vertices = list(range(1, 8))
edges = [[1, 3], [1, 2], [2, 3], [2, 4], [4, 5], [5, 6], [6, 7], [7, 4]]

visited = {}
for i in vertices:
    visited[i] = False

adj_list = {}
for u, v in edges:
    if u not in adj_list:
        adj_list[u] = []
    if v not in adj_list:
        adj_list[v] = []
    adj_list[u].append(v)
    adj_list[v].append(u)


def dfs(node, parent):
    visited[node] = True
    for adj_node in adj_list[node]:
        if not visited[adj_node]:
            dfs(adj_node, parent=node)
        elif adj_node != parent:
            print(f"back-edge from {adj_node} -> {node}")


for v in vertices:
    if not visited[v]:
        dfs(v, 0)

