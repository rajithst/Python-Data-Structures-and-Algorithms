from queue_ds.queue_ds import QueueDs


def bfs_traversal_helper(gp, src, destination, visited, distance):
    queue = QueueDs()
    queue.enqueue(src)
    visited[src] = True
    distance[src] = 0

    while not queue.is_empty():
        current_node = queue.dequeue()
        temp = gp.adj_list[current_node].head
        while temp is not None:
            if not visited[temp.val]:
                queue.enqueue(temp.val)
                visited[temp.val] = True
                distance[temp.val] = distance[current_node] + 1
                if temp.val == destination:
                    return distance
            temp = temp.next
    return distance


def shortest_path_find(graph, source, destination=-1):
    visited = {}
    distance = {}
    for i in graph.vertices:
        visited[i] = False
        distance[i] = 0

    distance = bfs_traversal_helper(graph, source, destination,visited, distance)
    for v in graph.vertices:
        if not visited[v]:
            distance = bfs_traversal_helper(graph, v, visited, distance)

    if destination != -1:
        print(distance[destination])
    else:
        print(distance)
