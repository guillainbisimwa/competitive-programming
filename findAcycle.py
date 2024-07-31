from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    #DFS
        def dfs(v, visited, parent):
            visited[v] = True
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    if dfs(neighbor, visited, v):
                        return True
                elif neighbor != parent:
                    return True
            return False	    
		#Code here
		visited = [False] * V
        
        for i in range(V):
            if not visited[i]:
                if dfs(i, visited, -1):
                    return True
        return False


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends