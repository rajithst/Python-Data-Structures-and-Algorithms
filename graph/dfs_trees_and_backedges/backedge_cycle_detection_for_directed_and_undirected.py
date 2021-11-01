vertices = list(range(1, 8))
edges = [[1, 3], [1, 2], [2, 3], [2, 4], [4, 5], [5, 6], [6, 7], [7, 4]]

# initially mark all nodes as 0 - not visited
visited = {}
for i in vertices:
    visited[i] = 0

adj_list = {}
for u, v in edges:
    if u not in adj_list:
        adj_list[u] = []
    if v not in adj_list:
        adj_list[v] = []
    adj_list[u].append(v)
    #adj_list[v].append(u)


def dfs(node, parent):
    # when visit to a node,mark as 1
    visited[node] = 1
    for adj_node in adj_list[node]:
        if not visited[adj_node]:
            dfs(adj_node, parent=node)
        # if node is visited, and node is not the parent,and node still in call-stack
        # which means trying to visit node that still in callstack,which means ancestor of current node
        # so it is a cycle and back-edge
        elif adj_node != parent and visited[adj_node] == 1:
            print("Cycle found")
            print(f"back-edge from {adj_node} -> {node}")

    # when leave the callstack,mark it as 2
    visited[node] = 2


for v in vertices:
    if not visited[v]:
        dfs(v, 0)