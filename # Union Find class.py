class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
		
    def union(self, x, y):
        m = self.find(x)
        n = self.find(y)
        
        if m != n:
            if self.size[m] > self.size[n]:
                self.root[n] = m
            elif self.size[m] < self.size[n]:
                self.root[m] = n
            else:
                self.root[n] = m
                self.size[m] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # True
print(uf.connected(5, 7))  # True
print(uf.connected(4, 9))  # False
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # True
