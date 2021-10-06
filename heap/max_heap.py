class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolate_up(len(self.heap) - 1)

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def __percolate_up(self, index):
        parent_index = (index - 1) // 2
        if index <= 0:
            return
        elif self.heap[parent_index] < self.heap[index]:
            tmp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[index]
            self.heap[index] = tmp
            self.__percolate_up(parent_index)


