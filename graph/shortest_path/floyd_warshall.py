def shortest_path_floyd_warshall(graph):
    vertices = len(graph[0])
    distance = graph.copy()

    for i in range(vertices):
        for j in range(vertices):
            for k in range(vertices):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance


def print_solution(distance):
    nV = len(distance[0])
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


# define inf as big value to avoid overflow
INF = 999
G = [[0, 3, INF, 5],
     [2, 0, INF, 4],
     [INF, 1, 0, INF],
     [INF, INF, 2, 0]]
result = shortest_path_floyd_warshall(G)
print_solution(result)