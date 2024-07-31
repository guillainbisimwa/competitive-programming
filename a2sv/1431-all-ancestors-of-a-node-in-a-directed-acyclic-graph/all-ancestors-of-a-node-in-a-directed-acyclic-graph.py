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
                
                # Decrement in-degree
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)
        
        return [sorted(list(ans)) for ans in answer]
                

       


