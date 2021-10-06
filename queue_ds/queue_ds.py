class QueueDs:
    def __init__(self):
        self.queue_list = []

    def is_empty(self):
        return len(self.queue_list) == 0

    def enqueue(self, val):
        self.queue_list.insert(0, val)

    def dequeue(self):
        if self.is_empty() is False:
            return self.queue_list.pop()
        return None

    def size(self):
        if not self.is_empty():
            return len(self.queue_list)
        return 0

    def front(self):
        if not self.is_empty():
            return self.queue_list[-1]
        return None

    def rear(self):
        if not self.is_empty():
            return self.queue_list[0]
        return None