class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert_node(self, new_value):
        self.insert(self.root, new_value)

    def insert(self, current_node, new_value):
        if current_node.data < new_value:
            if current_node.right:
                self.insert(current_node.right, new_value)
            else:
                current_node.right = Node(new_value)
        else:
            if current_node.left:
                self.insert(current_node.left, new_value)
            else:
                current_node.left = Node(new_value)

    def search_value(self, find_value):
        return self.search(self.root, find_value)

    def search(self, current_node, find_value):
        if current_node:
            if current_node.data == find_value:
                return True
            elif current_node.data < find_value:
                return self.search(current_node.right, find_value)
            else:
                return self.search(current_node.left, find_value)


bst = BinarySearchTree(10)
bst.insert_node(3)
bst.insert_node(1)
bst.insert_node(25)
bst.insert_node(9)
bst.insert_node(13)

print(bst.search_value(9))
print(bst.search_value(14))
