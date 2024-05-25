def maxValue(v):
    ans = []
    for _ in range(v):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        lower = 1
        high = 10**15
        while lower < high:
            mid = (lower + high + 1) >> 1
            n = sum(max(mid - ai, 0) for ai in a)
            if n <= x:
                lower = mid
            else:
                high = mid - 1
        ans.append(lower)
    return ans

v = int(input())
ans = maxValue(v)

for result in ans:
    print(result)
