from typing import List

class DSU:
    def __init__(self, n: int):
        self.par = [-1] * (n + 1)
        self.size = [1] * (n + 1)

    def findPar(self, u: int) -> int:
        if self.par[u] == -1:
            return u
        self.par[u] = self.findPar(self.par[u])
        return self.par[u]

    def unite(self, u: int, v: int) -> bool:
        # Unite two sets
        u = self.findPar(u)
        v = self.findPar(v)
        if u == v:
            return False
        if self.size[u] > self.size[v]:
            u, v = v, u  # Swap
        self.par[u] = v
        self.size[v] += self.size[u]
        return True


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        len_qs = len(queries)
        ans = [False] * len_qs
        dsu = DSU(n)

        # Sort  by distance
        edgeList.sort(key=lambda x: x[2])
        
        queries_with_index = [(q[0], q[1], q[2], idx) for idx, q in enumerate(queries)]
        queries_with_index.sort(key=lambda x: x[2])

        # Process each query
        j = 0
        for i in range(len_qs):
            while j < len(edgeList) and edgeList[j][2] < queries_with_index[i][2]:
                dsu.unite(edgeList[j][0], edgeList[j][1])
                j += 1
            
            ans[queries_with_index[i][3]] = dsu.findPar(queries_with_index[i][0]) == dsu.findPar(queries_with_index[i][1])

        return ans
