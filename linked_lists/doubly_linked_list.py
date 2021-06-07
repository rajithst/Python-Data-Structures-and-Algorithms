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

    def add_after_node(self,key,data):
        current_node = self.head
        while current_node:
            if current_node.next is None and current_node.data == key:
                self.append(data)
                return
            elif current_node.data == key:
                new_node = Node(data)
                next_node = current_node.next
                previous_node = current_node.prev

                current_node.next = new_node
                new_node.next = next_node
                new_node.prev = current_node
                next_node.prev = new_node
                return
            current_node = current_node.next


    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)
dllist.print_list()
print("-"*10)
dllist.add_after_node(2,110)

dllist.print_list()
