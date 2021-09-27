from queue.queue import Queue


def bfs_traversal_path_exist(graph,start,destination):
    visited = {}
    for i in graph.vertices:
        visited[i] = False

    # if destination not in visited.keys():
    #     return False

    queue = Queue()
    queue.enqueue(start)

    while not queue.is_empty():
        current_node = queue.dequeue()
        current_head = graph.adj_list[current_node].head

        while current_head:
            queue.enqueue(current_head.val)
            if not visited[current_head.val]:
                visited[current_head.val] = True
                if current_head.val == destination:
                    return True
            current_head = current_head.next

    return False
