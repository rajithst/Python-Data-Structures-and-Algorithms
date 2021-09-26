def count_edges(graph):
    edge_sum = 0
    for i in graph.vertices:
        head = graph.adj_list[i].head
        while head:
            edge_sum += 1
            head = head.next
    return edge_sum // 2
