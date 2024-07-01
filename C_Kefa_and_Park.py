def count_leaf_nodes_with_cats(n, m, cats, edges):
    cat_list = [0] + cats

    adjacency_list = [[] for _ in range(n + 1)]

    for edge in edges:
        u, v = edge
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    adjacency_list[1].append(0)

    result = 0
    stack = [(1, 0, 0)]

    while stack:
        node, consecutive_cats, parent = stack.pop()
        adjacency_list[node].remove(parent)
        
        if cat_list[node] == 1:
            consecutive_cats += 1
        else:
            consecutive_cats = 0
        
        if consecutive_cats > m:
            continue
        
        if not adjacency_list[node]:
            result += 1
        else:
            for neighbor in adjacency_list[node]:
                stack.append((neighbor, consecutive_cats, node))

    return result

n, m = map(int, input().split())
cats = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

print(count_leaf_nodes_with_cats(n, m, cats, edges))
