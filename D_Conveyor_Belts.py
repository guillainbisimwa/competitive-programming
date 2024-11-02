def min_energy_to_reach(t, n):
    results = []
    for case in n:
        n, x1, y1, x2, y2 = case
        
        layer1 = min(x1 - 1, y1 - 1, n - x1, n - y1)
        layer2 = min(x2 - 1, y2 - 1, n - x2, n - y2)
        
        energy = abs(layer1 - layer2)
        results.append(energy)
    
    return results

t = int(input().strip())
n = [tuple(map(int, input().strip().split())) for _ in range(t)]

results = min_energy_to_reach(t, n)

print("\n".join(map(str, results)))
