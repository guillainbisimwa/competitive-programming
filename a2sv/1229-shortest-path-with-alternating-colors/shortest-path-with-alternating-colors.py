class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = [[] for _ in range(n)]
        blue = [[] for _ in range(n)]
        
        for edge in redEdges:
            red[edge[0]].append(edge[1])
        
        for edge in blueEdges:
            blue[edge[0]].append(edge[1])
        
        # Init
        answer = [-1] * n
        
        queue = deque([(0, 0, -1)])  # -1 
        
        visit = set()
        visit.add((0, -1))
        
        #  BFS
        while queue:
            node, length, edgeColor = queue.popleft()
            
            if answer[node] == -1:
                answer[node] = length
            
            if edgeColor != 1:
                for neighbor in red[node]:
                    if (neighbor, 1) not in visit:
                        visit.add((neighbor, 1))
                        queue.append((neighbor, length + 1, 1))
            
            if edgeColor != 0:
                for neighbor in blue[node]:
                    if (neighbor, 0) not in visit:
                        visit.add((neighbor, 0))
                        queue.append((neighbor, length + 1, 0))
        
        return answer
        