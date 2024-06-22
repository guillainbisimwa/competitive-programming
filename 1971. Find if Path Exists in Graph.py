class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        stack = [source]
        visited = set([source])

        def DFS(self, v, visited):
            visited.add(v)
            for n in edges[v]:
                if n not in visited:
                    self.DFS(n, visited)

        self.DFS(source)
