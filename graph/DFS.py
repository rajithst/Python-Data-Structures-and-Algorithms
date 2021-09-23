from stack.stack import Stack


def dfs_traversal_helper(gp, src, visited):
    stack = Stack()
    stack.push(src)
    visited[src] = True
    results = ""
    while not stack.is_empty():
        current_node = stack.pop()
        results += str(current_node) + "=>"
        temp = gp.adj_list[current_node].head
        while temp is not None:
            if not visited[temp.val]:
                stack.push(temp.val)
                visited[temp.val] = True
            temp = temp.next
    return results, visited


def graph_dfs_traversal(graph, source):
    visited = {}
    for i in graph.vertices:
        visited[i] = False

    results, visited = dfs_traversal_helper(graph, source, visited)
    for v in graph.vertices:
        if not visited[v]:
            results_new, visited = dfs_traversal_helper(graph, v, visited)
            results += results_new

    print(visited)
    print(results)
