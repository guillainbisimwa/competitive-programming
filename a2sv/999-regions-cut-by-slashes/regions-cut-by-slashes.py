from typing import List

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UnionFind(4 * n * n)  # 4 triangles per cell

        for i in range(n):
            for j in range(n):
                root = 4 * (i * n + j)
                
                if grid[i][j] == '/':
                    uf.union(root + 0, root + 3)
                    uf.union(root + 1, root + 2)
                elif grid[i][j] == '\\':
                    uf.union(root + 0, root + 1)
                    uf.union(root + 2, root + 3)
                else:
                    uf.union(root + 0, root + 1)
                    uf.union(root + 1, root + 2)
                    uf.union(root + 2, root + 3)

                if i + 1 < n: 
                    uf.union(root + 2, root + 4 * n + 0)
                if j + 1 < n:  
                    uf.union(root + 1, root + 4 + 3)

        return sum(uf.find(x) == x for x in range(4 * n * n))

