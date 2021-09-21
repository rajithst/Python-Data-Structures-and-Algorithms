from queue.queue import Queue


def bfs_traversal_helper(gp, src, visited):
    queue = Queue()
    queue.enqueue(src)
    visited[src] = True
    results = ""
    while not queue.is_empty():
        current_node = queue.dequeue()
        results += str(current_node) + "=>"
        temp = gp.adj_list[current_node].head
        while temp is not None:
            if not visited[temp.val]:
                queue.enqueue(temp.val)
                visited[temp.val] = True
            temp = temp.next
    return results, visited


def graph_bfs_traversal(graph, source):
    visited = {}
    for i in graph.vertices:
        visited[i] = False

    results, visited = bfs_traversal_helper(graph, source, visited)
    for v in graph.vertices:
        if not visited[v]:
            results_new, visited = bfs_traversal_helper(graph, v, visited)
            results += results_new

    print(visited)
    print(results)
