t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    c = (n - 1) + (m - 1) * n
    if c == k:
        print("YES")
    else:
        print("NO")
