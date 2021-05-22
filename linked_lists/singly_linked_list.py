class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, previous_node, data):
        if not previous_node:
            print("Previous Node doesn't exist")
            return
        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def delete_by_value(self, value):
        curr_node = self.head
        if curr_node and curr_node.data == value:
            self.head = curr_node.next
            curr_node = None
            return

        previous_node = None
        while curr_node is not None and curr_node.data != value:
            previous_node = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        previous_node.next = curr_node.next
        curr_node = None

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("E")

llist.insert_after_node(llist.head.next, "F")
llist.print_list()
