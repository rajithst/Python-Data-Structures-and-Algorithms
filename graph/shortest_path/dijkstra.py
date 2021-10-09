import heapq as heap


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}
        for i in range(vertices):
            self.adj_list[i] = []

    def add_edge(self, u, v, w):
        self.adj_list[u].append((w, v))
        self.adj_list[v].append((w, u))


def shortest_path_dikstra(graph, src, dest):
    distance = [float("inf")] * graph.vertices
    distance[src] = 0
    pq = []
    heap.heappush(pq, (0, src))
    while pq:
        length_till_now, node = heap.heappop(pq)
        nbrs = graph.adj_list[node]
        for nei in nbrs:
            current_length = nei[0]
            current_node = nei[1]
            if length_till_now + current_length < distance[current_node]:
                distance[current_node] = length_till_now + current_length
                heap.heappush(pq, (distance[current_node], current_node))
    return distance[dest]


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
print(shortest_path_dikstra(g1, 0,4))
