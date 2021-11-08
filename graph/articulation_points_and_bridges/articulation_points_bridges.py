adj_list = {}
edges = [[1, 2], [1, 3], [2, 3], [2, 4], [4, 5], [5, 7], [7, 6], [4, 6]]
visited = {}
discovery = {}

for x, y in edges:
    if x not in adj_list:
        adj_list[x] = []
    if y not in adj_list:
        adj_list[y] = []

    visited[x] = False
    visited[y] = False
    adj_list[x].append(y)
    adj_list[y].append(x)

lowest_time = {}
time = 1
bridges = []
arp = set()


def dfs_tree(node, parent):
    global time
    visited[node] = True
    discovery[node] = lowest_time[node] = time
    time += 1
    child = 0
    for nd in adj_list[node]:
        if not visited[nd]:
            dfs_tree(nd, node)
            child += 1
            lowest_time[node] = min(lowest_time[node], lowest_time[nd])
            if lowest_time[nd] > discovery[node]:
                bridges.append((node, nd))

            if parent != 0 and lowest_time[nd] >= discovery[node]:
                arp.add(node)

        elif nd != parent:
            # back edge found
            lowest_time[node] = min(lowest_time[node], discovery[nd])
    if parent == 0 and child > 1:
        arp.add(node)

dfs_tree(1,0)