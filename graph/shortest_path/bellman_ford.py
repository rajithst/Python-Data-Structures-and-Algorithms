class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edge_list = []

    def add_edge(self, u, v, w):
        self.edge_list.append((w, u, v))


def shortest_path_bellman_ford(graph, src):
    # initialize all path lengths as inf
    distance = [float("inf")] * graph.vertices
    distance[src] = 0
    # relaxing all edges v-1 times
    for i in range(graph.vertices - 1):
        for edge in graph.edge_list:
            weight = edge[0]
            from_edge = edge[1]
            to_edge = edge[2]
            # if short path found than current distance,update distance array
            if distance[from_edge] != float("inf") and distance[from_edge] + weight < distance[to_edge]:
                distance[to_edge] = distance[from_edge] + weight

    # after v-1 relaxation,run another relaxation round to check if negative weighted cycle exist
    for edge in graph.edge_list:
        weight = edge[0]
        from_edge = edge[1]
        to_edge = edge[2]
        if distance[from_edge] != float("inf") and distance[from_edge] + weight < distance[to_edge]:
            print("Negative weight cycle Found!!")
            return

    for idx,v in enumerate(distance):
        print(f"Node 0 -> {idx} distance {v}")
    return distance


g1 = Graph(3)
g1.add_edge(0, 1, 3)
g1.add_edge(1, 2, 4)
g1.add_edge(0, 2, -10)
print(shortest_path_bellman_ford(g1,0))
