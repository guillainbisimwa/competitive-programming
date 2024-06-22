n = int(input())
 
adj = [[] for _ in range(n)] 
 
for _ in range(n-1):
    a, b = [int(x) for x in input().split()]
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)
 
red = []
blue = 0
 
visited = [False] * n
 
def dfs(node, c):
    global blue
    visited[node] = True
    if c:
        red.append(node)
    else:
        blue += 1
    for child in adj[node]:
        if not visited[child]:
            dfs(child, 1-c)
 
dfs(0, 0)
 
total = 0
 
for n1 in red:
    total += max(0, blue-len(adj[n1]))
        
print(total)