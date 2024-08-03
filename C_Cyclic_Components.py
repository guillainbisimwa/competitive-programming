from collections import deque

def findCycle(n, m):
    
    graph = {i: [] for i in range(1, n + 1)}
    degree = {i: 0 for i in range(1, n + 1)}
    
    for a, b in m:
        graph[a].append(b)
        graph[b].append(a)
        degree[a] += 1
        degree[b] += 1
    
    visited = {i: False for i in range(1, n + 1)}
    component = {}

    for i in range(1, n + 1):
        if not visited[i]:
            #  BFS
            queue = deque()
            queue.append(i)
            visited[i] = True
            component[i] = [i]
            
            while queue:
                v = queue.popleft()  
                for u in graph[v]: 
                    if not visited[u]:
                        visited[u] = True
                        component[i].append(u) 
                        queue.append(u)
    
    count = 0
    for comp in component.values():
        is_cycle = all(degree[node] == 2 for node in comp)
        if is_cycle:
            count += 1
    
    return print(count)

n,s = map(int, input().split())
m = [tuple(map(int, input().split())) for _ in range(s)]
findCycle(n,m)
