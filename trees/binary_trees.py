class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)

    """
    Tree traversal - depth first
    """
    def preorder_traversal(self,start,traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_traversal(start.left,traversal)
            traversal = self.preorder_traversal(start.right,traversal)
        return traversal

    def inorder_traversal(self,start,traversal):
        if start:
            traversal = self.inorder_traversal(start.left,traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_traversal(start.right,traversal)
        return traversal

    def postorder_traversal(self,start,traversal):
        if start:
            traversal = self.postorder_traversal(start.left,traversal)
            traversal = self.postorder_traversal(start.right,traversal)
            traversal += (str(start.value) + "-")
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.preorder_traversal(tree.root,""))
print(tree.inorder_traversal(tree.root,""))
print(tree.postorder_traversal(tree.root,""))