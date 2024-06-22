def dfs(graph, node, visited):
    stack = [node]
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)

x, y = [int(num) for num in input().strip().split()]
f = [input().strip() for _ in range(x)]

for i in range(x):
    for j in range(1, y):
        if f[i][j] != f[i][j - 1]:
            print("NO")
            exit()

graph = {i: [] for i in range(x)}
for i in range(1, x):
    if f[i][0] == f[i - 1][0]:
        graph[i].append(i - 1)
        graph[i - 1].append(i)

visited = [False] * x
for i in range(x):
    if not visited[i]:
        dfs(graph, i, visited)

for i in range(1, x):
    if f[i][0] == f[i - 1][0]:
        print("NO")
        exit()

print("YES")
