from trees.stack import Stack
from trees.queue import Queue


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    """
    Tree traversal - depth first
    """

    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    """
    level order traversal
    """

    def level_order_traversal(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_level_order_traversal(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
        return traversal

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def size(self, node):
        if node is None:
            return 0
        return 1 + (self.size(node.left) + self.size(node.right))

    def size_using_stack(self):
        if self.root is None:
            return 0
        stack = Stack()
        stack.push(self.root)
        count = 1
        while stack:
            node = stack.pop()
            if node.left:
                count += 1
                stack.push(node.left)
            if node.right:
                count += 1
                stack.push(node.right)
        return count


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.size(tree.root))
print(tree.size_using_stack())
