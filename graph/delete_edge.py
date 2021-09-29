def delete_edge(graph, start, end):
    if start == end:
        return
    current_node = graph.adj_list[start].head
    previous_node = None
    while current_node:
        if current_node.val == end:
            if previous_node is None:
                graph.adj_list[start].head = current_node.next
                current_node.next = None
            else:
                previous_node.next = current_node.next
                current_node.next = None
            return
        previous_node = current_node
        current_node = current_node.next
    return
