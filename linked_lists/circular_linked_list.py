class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinekdList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            current_node = self.head
            new_node = Node(data)
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head
