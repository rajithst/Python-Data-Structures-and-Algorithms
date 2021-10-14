class DisjoinSet:
    def __init__(self, size):
        self.root = [-1] * size
        self.rank = [1] * size

    def find(self, node):
        if self.root[node] == -1:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_v != root_u:
            if self.rank[root_u] > self.rank[root_v]:
                self.root[root_v] = root_u
                self.rank[root_u] += self.rank[root_v]
            else:
                self.root[root_u] = root_v
                self.rank[root_v] += self.rank[root_u]


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edge_list = []

    def add_edge(self, u, v, w):
        self.edge_list.append((u, v, w))
        self.edge_list.append((v, u, w))


def minimum_spanning_tree_kruskal(graph):
    #sort all edges from weight
    sorted_edge_list = sorted(graph.edge_list, key=lambda item: item[2])
    #initialize disjoint set
    dsu = DisjoinSet(graph.vertices)
    mst_weight = 0
    #iterate through each edge
    for edge in sorted_edge_list:
        from_node = edge[0]
        to_node = edge[1]
        weight = edge[2]
        #if edge is not create a cycle,add weight and add edge to mst by union it
        if dsu.find(from_node) != dsu.find(to_node):
            dsu.union(from_node,to_node)
            mst_weight += weight
    return mst_weight

g1 = Graph(7)
g1.add_edge(0, 1, 28)
g1.add_edge(0, 5, 10)
g1.add_edge(1, 6, 14)
g1.add_edge(5, 4, 25)
g1.add_edge(4, 6, 24)
g1.add_edge(4, 3, 22)
g1.add_edge(3, 2, 12)
g1.add_edge(3, 6, 18)
g1.add_edge(1, 2, 16)
print(minimum_spanning_tree_kruskal(g1))
