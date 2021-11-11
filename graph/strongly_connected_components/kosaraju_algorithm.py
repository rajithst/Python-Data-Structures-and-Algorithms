graph = {}
graph_reverse = {}
edges = [[1, 2], [2, 3], [3, 1], [3, 4]]
visited = {}
visited_copy = {}
component_color = {}
for x, y in edges:
    visited[x] = False
    visited[y] = False

    visited_copy[x] = False
    visited_copy[y] = False

    component_color[x] = 0
    component_color[y] = 0

    if x not in graph:
        graph[x] = []
    graph[x].append(y)
    if y not in graph_reverse:
        graph_reverse[y] = []
    graph_reverse[y].append(x)

topological_order = []


def dfs(node):
    visited[node] = True
    if node in graph:
        for adj in graph[node]:
            if not visited[adj]:
                dfs(adj)
    topological_order.append(node)


def make_topological_order():
    for node in visited.keys():
        if not visited[node]:
            dfs(node)
    return list(reversed(topological_order))




def dfs2(node, component):
    visited_copy[node] = True
    component_color[node] = component
    if node in graph_reverse:
        for adj in graph_reverse[node]:
            if not visited_copy[adj]:
                dfs2(adj, component)

tporder = make_topological_order()
sc_components = 1
for node in tporder:
    if not visited_copy[node]:
        dfs2(node, sc_components)
        sc_components += 1
print(component_color)
