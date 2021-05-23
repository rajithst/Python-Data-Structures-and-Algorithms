class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    """
    Insert operations
    """
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

    """
    delete operations
    """
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

    def delete_by_position(self,position):
        if self.head:
            curr_node = self.head
            if position==0:
                self.head = curr_node.next
                curr_node = None
                return
            previous_node = None
            count = 0
            while count != position:
                previous_node = curr_node
                curr_node = curr_node.next
                count+=1
            if curr_node is None:
                return
            previous_node.next = curr_node.next
            curr_node = None

    """
    get length
    """
    def lenght_of_linked_list(self):
        curr_node = self.head
        count = 0
        while curr_node is not None:
            curr_node = curr_node.next
            count+=1
        return count

    def length_of_linked_list_recursive(self,node):
        if node is None:
            return 0
        return 1 + self.length_of_linked_list_recursive(node.next)


    """
    swap nodes
    """
    def swap_nodes(self,val1,val2):

        curr_node_1 = self.head
        previous_node_1 = None
        while curr_node_1 and curr_node_1.data != val1:
            previous_node_1 = curr_node_1
            curr_node_1 = curr_node_1.next

        curr_node_2 = self.head
        previous_node_2 = None
        while curr_node_2 and curr_node_2.data != val2:
            previous_node_2 = curr_node_2
            curr_node_2 = curr_node_2.next

        if not curr_node_1 or not curr_node_2:
            return

        if previous_node_1:
            previous_node_1.next = curr_node_2
        else:
            self.head = curr_node_2

        if previous_node_2:
            previous_node_2.next = curr_node_1
        else:
            self.head = curr_node_1

        curr_node_1.next,curr_node_2.next = curr_node_2.next,curr_node_1.next

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
llist.append("E")

llist.swap_nodes("C","D")
llist.print_list()
