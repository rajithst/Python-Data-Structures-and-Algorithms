adj_list = {}
edges = [[1, 2], [1,5], [2,5], [2, 4], [3,1],[3,2]]
visited = {}
for x, y in edges:
    if x not in adj_list:
        adj_list[x] = []
    visited[x] = False
    visited[y] = False
    adj_list[x].append(y)

tp_order = []


def dfs(node):
    visited[node] = True
    if node in adj_list:
        for adj in adj_list[node]:
            if not visited[adj]:
                dfs(adj)
    tp_order.append(node)


def topological_order():
    for node in visited.keys():
        if not visited[node]:
            dfs(node)
    print(list(reversed(tp_order)))

topological_order()