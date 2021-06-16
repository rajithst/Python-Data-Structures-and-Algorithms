class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert_node(self, new_value):
        if self.root is None:
            self.root = Node(new_value)
        else:
            self.insert(new_value, self.root)

    def insert(self, new_value, current_node):

        if new_value < current_node.data:
            if current_node.left is None:
                current_node.left = Node(new_value)
            else:
                self.insert(new_value, current_node.left)
        elif new_value > current_node.data:
            if current_node.right is None:
                current_node.right = Node(new_value)
            else:
                self.insert(new_value, current_node.right)

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

    def is_valid_bts(self):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.data
            if val <= lower or val >= upper:
                return False
            if not helper(node.right, lower=val, upper=upper):
                return False
            if not helper(node.left, lower=lower, upper=val):
                return False
            return True

        return helper(self.root)


bst = BinarySearchTree(4)
bst.insert_node(2)
bst.insert_node(8)
bst.insert_node(5)
bst.insert_node(10)


tree = BinarySearchTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(bst.is_valid_bts())
print(tree.is_valid_bts())
