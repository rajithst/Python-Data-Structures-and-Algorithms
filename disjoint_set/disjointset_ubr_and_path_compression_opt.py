class UnionFind:
    def __init__(self, size):
        self.root = [-1] * size
        self.rank = [1] * size

    def find(self, node):
        if self.root[node] == -1:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union_by_rank(self, u, v):
        root_x = self.find(u)
        root_y = self.find(v)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
                self.rank[root_y] += self.rank[root_x]
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += self.rank[root_y]
        else:
            print("Both in same set")

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


uf = UnionFind(7)

uf.union_by_rank(0, 1)
uf.union_by_rank(1, 2)
uf.union_by_rank(2, 3)
print(uf.root)
print(uf.rank)
uf.union_by_rank(4, 5)
uf.union_by_rank(5, 6)
print(uf.root)
print(uf.rank)
uf.union_by_rank(2, 5)
print("-" * 20)
print(uf.root)
print(uf.rank)
print(uf.is_connected(2, 5))
print(uf.find(6))
