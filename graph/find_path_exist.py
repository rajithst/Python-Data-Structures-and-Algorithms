from queue_ds.queue_ds import QueueDs
from stack.stack import Stack


def dfs_traversal_path_exist(graph, start, destination):
    if start == destination:
        return True
    visited = {}
    for i in graph.vertices:
        visited[i] = False

    stack = Stack()
    stack.push(start)
    visited[start] = True

    while not stack.is_empty():
        current_node = stack.pop()
        temp = graph.adj_list[current_node].head
        while temp is not None:
            if not visited[temp.val]:
                stack.push(temp.val)
                visited[temp.val] = True
                if temp.val == destination:
                    return True
            temp = temp.next
    return False


def bfs_traversal_path_exist(graph, start, destination):
    if start == destination:
        return True
    visited = {}
    for i in graph.vertices:
        visited[i] = False

    queue = QueueDs()
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
