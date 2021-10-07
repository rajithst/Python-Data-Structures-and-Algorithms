class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolate_up(len(self.heap) - 1)

    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None

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
        elif self.heap[parent_index] > self.heap[index]:
            tmp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[index]
            self.heap[index] = tmp
            self.__percolate_up(parent_index)

    def __min_heapify(self, index):
        smallest = index
        left_index = (index * 2) + 1
        right_index = (index * 2) + 2

        if len(self.heap) > left_index and self.heap[smallest] > self.heap[left_index]:
            smallest = left_index
        if len(self.heap) > right_index and self.heap[smallest] > self.heap[right_index]:
            smallest = right_index
        if smallest != index:
            tmp = self.heap[smallest]
            self.heap[smallest] = self.heap[index]
            self.heap[index] = tmp
            self.__min_heapify(smallest)
