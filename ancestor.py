from collections import deque
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        answer = [set() for _ in range(n)]
        
        # Build the graph
        for n1, n2 in edges:
            graph[n1].append(n2)
        
        inDegree = [0] * n
        for node in range(n):
            for nei in graph[node]:
                inDegree[nei] += 1

        queue = deque()

        for node in range(n):
            if inDegree[node] == 0:
                queue.append(node)
        
        # BFS
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                # Ancestor list
                for ancestor in answer[node]:
                    answer[nei].add(ancestor)
                answer[nei].add(node)
                
                # Debugging print statements
                print(f"Node: {node}, Neighbor: {nei}, Ancestors of Neighbor: {sorted(list(answer[nei]))}")

                # Decrement in-degree
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)
        
        return [sorted(list(ans)) for ans in answer]

# Test case
n = 9
edges = [[3,6],[2,4],[8,6],[7,4],[1,4],[2,1],[7,2],[0,4],[5,0],[4,6],[3,2],[5,6],[1,6]]
solution = Solution()
output = solution.getAncestors(n, edges)
print(f"Output: {output}")



# Node: 3, Neighbor: 6, Ancestors of Neighbor: [3]
# Node: 3, Neighbor: 2, Ancestors of Neighbor: [3]
# Node: 5, Neighbor: 0, Ancestors of Neighbor: [5]
# Node: 5, Neighbor: 6, Ancestors of Neighbor: [3, 5]
# Node: 7, Neighbor: 4, Ancestors of Neighbor: [7]
# Node: 7, Neighbor: 2, Ancestors of Neighbor: [3, 7]
# Node: 8, Neighbor: 6, Ancestors of Neighbor: [3, 5, 8]
# Node: 0, Neighbor: 4, Ancestors of Neighbor: [0, 5, 7]
# Node: 2, Neighbor: 4, Ancestors of Neighbor: [0, 2, 3, 5, 7]
# Node: 2, Neighbor: 1, Ancestors of Neighbor: [2, 3, 7]
# Node: 1, Neighbor: 4, Ancestors of Neighbor: [0, 1, 2, 3, 5, 7]
# Node: 1, Neighbor: 6, Ancestors of Neighbor: [1, 2, 3, 5, 7, 8]
# Node: 4, Neighbor: 6, Ancestors of Neighbor: [0, 1, 2, 3, 4, 5, 7, 8]
# Output: [[5], [2, 3, 7], [3, 7], [], [0, 1, 2, 3, 5, 7], [], [0, 1, 2, 3, 4, 5, 7, 8], [], []]
