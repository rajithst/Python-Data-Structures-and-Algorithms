class NodeE:
    def __init__(self, val):
        self.val = val
        self.neighbours = []


def clone_graph(start, graph):
    copy_map = {}

    def clone(node):
        if node in copy_map:
            return copy_map[node]

        copy = NodeE(node)
        copy_map[node] = copy
        neighbour = graph.adj_list[node].head
        while neighbour:
            copy.neighbours.append(clone(neighbour.val))
            neighbour = neighbour.next
        return copy

    if start is None:
        return
    return clone(start)
