from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def count_beautiful_paths(n, colors, edges):
    # Build the adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Track visited colors
    visited = [False] * (n + 1)
    result = [0]

    def dfs(node, parent, start_color):
        visited[node] = True
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            if colors[neighbor - 1] == start_color:
                result[0] += 1
            elif not visited[neighbor]:
                dfs(neighbor, node, start_color)
        visited[node] = False

    # Iterate over all nodes and start a DFS for each unique color
    for start in range(1, n + 1):
        visited[start] = True
        for neighbor in adj[start]:
            if colors[neighbor - 1] == colors[start - 1]:
                result[0] += 1
            else:
                dfs(neighbor, start, colors[start - 1])
        visited[start] = False
    
    return result[0] // 2  # Each path is counted twice

def main():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        colors = list(map(int, data[index:index + n]))
        index += n
        edges = []
        for _ in range(n - 1):
            u, v = map(int, data[index:index + 2])
            index += 2
            edges.append((u, v))
        
        results.append(count_beautiful_paths(n, colors, edges))
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
