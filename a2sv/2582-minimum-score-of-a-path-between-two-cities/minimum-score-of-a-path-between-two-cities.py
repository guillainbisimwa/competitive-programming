class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()

        for v1, v2, distance in roads:
            graph[v1].append((v2, distance))
            graph[v2].append((v1, distance))

        queue = deque([1])
        visited.add(1)
        ans = float('inf')

        # BFS
        while queue:
            node = queue.popleft()
            for next_node, distance in graph[node]:
                ans = min(ans, distance)
                if next_node in visited:
                    continue

                visited.add(next_node)
                queue.append(next_node)

        return ans
