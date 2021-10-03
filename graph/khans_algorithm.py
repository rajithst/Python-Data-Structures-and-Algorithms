from collections import deque


def calculate_indegrees(graph):
    indegrees = {}
    for v in graph.vertices:
        indegrees[v] = 0
        head = graph.adj_list[v].head
        while head:
            if head.val not in indegrees:
                indegrees[head.val] = 0
            indegrees[head.val] += 1
            head = head.next
    return indegrees


def topological_sort_bfs(graph):
    # calculate indegree for each vertices
    indegrees = calculate_indegrees(graph)
    queue = deque()
    for v in graph.vertices:
        if indegrees[v] == 0:
            queue.append(v)

    # iterate over queue to topological sort
    result = ""
    while queue:
        current_node = queue.popleft()
        result += str(current_node) + " => "
        nei = graph.adj_list[current_node].head
        while nei:
            indegrees[nei.val] -= 1
            if indegrees[nei.val] == 0:
                queue.append(nei.val)
            nei = nei.next
    return result
