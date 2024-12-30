import heapq
import sys

def find_min_cost(t, p):
    results = []
    for case in p:
        n, m, k, d, grid = case
        min_costs = []

        for row in grid:
            heap, cost = [], 0
            heapq.heappush(heap, (1, 0))
            for i in range(1, m):
                while heap and heap[0][1] < i - d - 1:
                    heapq.heappop(heap)
                cost = row[i] + 1 + heap[0][0]
                heapq.heappush(heap, (cost, i))
            min_costs.append(cost)

        min_sum = sum(min_costs[:k])
        min_cost = min_sum

        for i in range(k, n):
            min_sum += min_costs[i] - min_costs[i - k]
            min_cost = min(min_cost, min_sum)

        results.append(min_cost)
    return results

T = int(sys.stdin.readline().strip())
p = []
for _ in range(T):
    n, m, k, d = map(int, sys.stdin.readline().strip().split())
    grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    p.append((n, m, k, d, grid))

for result in find_min_cost(T, p):
    print(result)
