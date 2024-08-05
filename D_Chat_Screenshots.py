from collections import deque

def solve(data):
    
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        
        G = [[] for _ in range(n + 1)]
        a = [0] * (n + 1)
        d = [0] * (n + 1)
        
        for _ in range(k):
            for i in range(1, n + 1):
                a[i] = int(data[index])
                index += 1
                if i >= 3:
                    G[a[i - 1]].append(a[i])
                    d[a[i]] += 1
        
        q = deque()
        for i in range(1, n + 1):
            if d[i] == 0:
                q.append(i)
        
        ans = 0
        while q:
            ans += 1
            u = q.popleft()
            for v in G[u]:
                d[v] -= 1
                if d[v] == 0:
                    q.append(v)
        
        if ans == n:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))
import sys
input = sys.stdin.read
data = input().split()
solve(data)
