class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def add_after_node(self, key, data):
        current_node = self.head
        while current_node:
            if current_node.next is None and current_node.data == key:
                self.append(data)
                return
            elif current_node.data == key:
                new_node = Node(data)
                next_node = current_node.next

                current_node.next = new_node
                new_node.next = next_node
                new_node.prev = current_node
                next_node.prev = new_node
                return
            current_node = current_node.next

    def add_before_node(self, key, data):
        current_node = self.head
        while current_node:
            if current_node.next is None and current_node.data == key:
                self.append(data)
                return
            elif current_node.data == key:
                new_node = Node(data)
                previous_node = current_node.prev

                previous_node.next = new_node
                new_node.prev = previous_node
                new_node.next = current_node
                current_node.prev = new_node
                return
            current_node = current_node.next

    def delete(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key and current_node == self.head:
                if not current_node.next:
                    current_node = None
                    self.head = None
                    return
                else:
                    next_node = current_node.next
                    current_node.next = None
                    next_node.prev = None
                    current_node = None
                    self.head = next_node
                    return
            elif current_node.data == key:
                if current_node.next:
                    next_node = current_node.next
                    previous_node = current_node.prev

                    previous_node.next = next_node
                    next_node.prev = previous_node
                    current_node.next = None
                    current_node.prev = None
                    current_node = None
                    return
                else:
                    previous_node = current_node.prev
                    previous_node.next = None
                    current_node.prev = None
                    current_node = None
                    return
            current_node = current_node.next

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

dllist.delete(1)
dllist.delete(6)
dllist.delete(4)

dllist.delete(3)
dllist.print_list()
