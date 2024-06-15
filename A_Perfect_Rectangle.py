import math
import sys


def can_form_square_grid(n, marbles):
    total_marbles = sum(marbles)
    sqrt_total = int(math.isqrt(total_marbles))
    return sqrt_total * sqrt_total == total_marbles

input = sys.stdin.read
data = input().split()

idx = 0
t = int(data[idx])
idx += 1
results = []

for _ in range(t):
    n = int(data[idx])
    idx += 1
    marbles = list(map(int, data[idx:idx + n]))
    idx += n
    
    if can_form_square_grid(n, marbles):
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(results))


