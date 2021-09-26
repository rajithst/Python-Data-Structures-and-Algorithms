from queue.queue import Queue


def bfs_traversal_helper(gp, src, visited, distance):
    queue = Queue()
    queue.enqueue(src)
    visited[src] = True
    distance[src] = 0
    results = ""
    while not queue.is_empty():
        current_node = queue.dequeue()
        results += str(current_node) + "=>"
        temp = gp.adj_list[current_node].head
        while temp is not None:
            if not visited[temp.val]:
                queue.enqueue(temp.val)
                visited[temp.val] = True
                distance[temp.val] = distance[current_node] + 1
            temp = temp.next
    return results, visited, distance


def shortest_path_find(graph, source, destination=-1):
    visited = {}
    distance = {}
    for i in graph.vertices:
        visited[i] = False
        distance[i] = 0

    results, visited, distance = bfs_traversal_helper(graph, source, visited, distance)
    for v in graph.vertices:
        if not visited[v]:
            results_new, visited, distance = bfs_traversal_helper(graph, v, visited, distance)
            results += results_new

    if destination != -1:
        print(distance[destination])
    else:
        print(distance)
