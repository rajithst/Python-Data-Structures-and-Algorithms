vertices = list(range(1, 8))
edges = [[1, 2], [1, 3], [2, 4], [2, 5], [2, 6], [4, 10], [5, 8], [8, 9], [8, 11], [3, 7], [7, 12]]

# create adjacency list
adj_list = {}
for u, v in edges:
    if u not in adj_list:
        adj_list[u] = []
    if v not in adj_list:
        adj_list[v] = []
    adj_list[u].append(v)
    adj_list[v].append(u)

# define empty dictionary to store  parent nodes and depth of each node
parent = {}
depth = {}


# define depth first search to find depth of each node and parent of each node
def dfs(node, par):
    parent[node] = par
    depth[node] = 0 if par == 0 else depth[par] + 1
    for nei in adj_list[node]:
        if nei != par:
            dfs(nei, node)

# define function to find lowest common ancestor
def lca(u, v):
    # if u and v are same, return u
    if u == v:
        return u
    # always get u as deepest node,if depth of u is less than v, swap them
    if depth[u] < depth[v]:
        u, v = v, u
    # move u to v's depth
    diff = depth[u] - depth[v]
    while diff > 0:
        u = parent[u]
        diff -= 1
    # at this point, u is at v's depth, so move both u and v top while they come to same node
    # first node both u and v come to same node is the lowest common ancestor
    while u != v:
        u = parent[u]
        v = parent[v]
    return u


dfs(1, 0)
print(lca(9, 12))
