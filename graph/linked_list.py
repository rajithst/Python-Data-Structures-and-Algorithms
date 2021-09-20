from graph.node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        temp_node = Node(val)
        if self.is_empty():
            self.head = temp_node
            return self.head
        temp_node.next = self.head
        self.head = temp_node
        return self.head

    def insert_at_tail(self, val):
        if self.is_empty():
            self.head = Node(val)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(val)

    def get_head(self):
        return self.head

    def is_empty(self):
        return self.head is None
