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

    def remove_max(self):
        if len(self.heap) > 1:
            max_val = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__max_heapify(index=0)
            return max_val
        elif len(self.heap) == 1:
            max_val = self.heap[0]
            del self.heap[0]
            return max_val
        else:
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

    def __max_heapify(self, index):
        largest = index
        left_index = index * 2 + 1
        right_index = index * 2 + 2

        if len(self.heap) > left_index and self.heap[largest] < self.heap[left_index]:
            largest = left_index
        if len(self.heap) > right_index and self.heap[largest] < self.heap[right_index]:
            largest = right_index
        if largest != index:
            tmp = self.heap[largest]
            self.heap[largest] = self.heap[index]
            self.heap[index] = tmp
            self.__max_heapify(largest)
