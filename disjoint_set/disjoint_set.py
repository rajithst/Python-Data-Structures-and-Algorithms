class UnionFind:
    def __init__(self, size):
        self.root = [-1] * size

    def find(self, node):
        if self.root[node] == -1:
            return node
        return self.find(self.root[node])

    def quick_union(self, u, v):
        root_x = self.find(u)
        root_y = self.find(v)

        if root_x != root_y:
            self.root[root_y] = root_x
        else:
            print("Both in same set")

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


uf = UnionFind(6)

uf.quick_union(0, 1)
uf.quick_union(1, 2)
print(uf.root)
uf.quick_union(3,4)
uf.quick_union(4,5)
print(uf.root)
uf.quick_union(2,5)
print(uf.root)
print(uf.is_connected(2,5))