class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        current_node = self.head
        count = 0
        while current_node:
            count+=1
            current_node = current_node.next
            if current_node == self.head:
                break
        return count

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

    def prepend(self, data):
        new_node = Node(data)
        current_node = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
        self.head = new_node

    def delete_node(self, data):
        if self.head:
            if self.head.data == data:
                current_node = self.head
                while current_node.next != self.head:
                    current_node = current_node.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    current_node.next = self.head.next
                    self.head = self.head.next
            else:
                current_node = self.head
                previous_node = None
                while current_node.next != self.head:
                    previous_node = current_node
                    current_node = current_node.next
                    if current_node.data == data:
                        previous_node.next = current_node.next
                        current_node = current_node.next


    def split_list(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size//2
        count = 0
        current_node = self.head
        previous_node = None
        while current_node and count < mid:
            previous_node = current_node
            current_node = current_node.next
            count+=1
        previous_node.next = self.head

        new_cllist = CircularLinkedList()
        while current_node.next != self.head:
            new_cllist.append(current_node.data)
            current_node = current_node.next
        new_cllist.append(current_node.data)
        self.print_list()
        print("\n")
        new_cllist.print_list()

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break


cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.append("E")
cllist.append("F")
cllist.split_list()


