vertices = [0, 1, 2, 3, ]
visited = {v: False for v in vertices}
edges = [(0, 1), (1, 2), (1, 3), (3, 2)]
adj_list = {}
for x, y in edges:
    if x not in adj_list:
        adj_list[x] = []
    if y not in adj_list:
        adj_list[y] = []
    adj_list[x].append(y)
    adj_list[y].append(x)


def dfs(node, parent):
    visited[node] = True
    for nei in adj_list[node]:
        if not visited[nei]:
            cycle_found = dfs(nei, parent=node)
            if cycle_found:
                return True
        elif nei != parent:
            return True
    return False


def dfs_wrapper():
    for v in vertices:
        if not visited[v]:
            if dfs(v,-1):
                return "Cycle Found"
    return "Cycle Not Found"
