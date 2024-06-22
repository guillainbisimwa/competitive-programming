def dfs(node, parent, level, prop, g, init, goal):
    init[node] = (init[node] + prop[level]) % 2
    toggle_count = 0
    
    if init[node] != goal[node]:
        print(node + 1)
        prop[level] = (prop[level] + 1) % 2
        toggle_count += 1
    
    for neighbor in g[node]:
        if neighbor != parent:
            toggle_count += dfs(neighbor, node, 1 - level, prop[:], g, init, goal)
    
    return toggle_count

n = int(input())

g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

init = list(map(int, input().split()))
goal = list(map(int, input().split()))

start_node = 0
initial_prop = [0, 0]

toggle_count = dfs(start_node, -1, 0, initial_prop, g, init, goal)

print(toggle_count)
