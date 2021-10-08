class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, node):
        self.heap.append(node)
        self.__percolate_up(len(self.heap) - 1)

    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None

    def is_empty(self):
        return len(self.heap) == 0

    def remove_min(self):
        if len(self.heap) > 1:
            min_val = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__min_heapify(index=0)
            return min_val

        elif len(self.heap) == 1:
            min_val = self.heap[0]
            del self.heap[0]
            return min_val
        else:
            return None

    def __percolate_up(self, index):
        parent_index = (index - 1) // 2
        if index <= 0:
            return
        elif self.heap[parent_index][1] > self.heap[index][1]:
            tmp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[index]
            self.heap[index] = tmp
            self.__percolate_up(parent_index)

    def __min_heapify(self, index):
        smallest = index
        left_index = (index * 2) + 1
        right_index = (index * 2) + 2

        if len(self.heap) > left_index and self.heap[smallest][1] > self.heap[left_index][1]:
            smallest = left_index
        if len(self.heap) > right_index and self.heap[smallest][1] > self.heap[right_index][1]:
            smallest = right_index
        if smallest != index:
            tmp = self.heap[smallest]
            self.heap[smallest] = self.heap[index]
            self.heap[index] = tmp
            self.__min_heapify(smallest)


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}
        for i in range(vertices):
            self.adj_list[i] = []

    def add_edge(self, u, v, w):
        self.adj_list[u].append((v, w))
        self.adj_list[v].append((u, w))


def minimum_spanning_tree_prims(graph):
    priority_queue = MinHeap()
    visited = {}
    for v in range(graph.vertices):
        visited[v] = False
    mst_weight = 0
    # node = ( node value,weight)
    node = (0, 0)
    result = ""
    priority_queue.insert(node)
    while not priority_queue.is_empty():
        best_node = priority_queue.remove_min()
        to_edge = best_node[0]
        weight = best_node[1]
        if visited[to_edge]:
            continue
        result += str(to_edge) + " => "
        mst_weight += weight
        visited[to_edge] = True
        for edges in graph.adj_list[to_edge]:
            if not visited[edges[0]]:
                priority_queue.insert(edges)
    print(result)
    return mst_weight


g1 = Graph(7)
g1.add_edge(0, 1, 28)
g1.add_edge(0, 5, 10)
g1.add_edge(1, 6, 14)
g1.add_edge(5, 4, 25)
g1.add_edge(4, 6, 24)
g1.add_edge(4, 3, 22)
g1.add_edge(3, 2, 12)
g1.add_edge(3, 6, 18)
g1.add_edge(1, 2, 16)
print(minimum_spanning_tree_prims(g1))
