from stack.stack import Stack


def find_mother_vertex_naive(graph):
    for i in graph.vertices:
        num_of_vertices_reached = perform_dfs(i, graph)
        if sum(num_of_vertices_reached) == len(graph.vertices):
            return i
    return -1


def perform_dfs(vertex, graph):
    visited = [False] * len(graph.vertices)
    stack = Stack()
    stack.push(vertex)
    visited[vertex] = True

    while not stack.is_empty():
        current_node = stack.pop()
        temp = graph.adj_list[current_node].head
        while temp is not None:
            if not visited[temp.val]:
                stack.push(temp.val)
                visited[temp.val] = True
            temp = temp.next
    return visited



