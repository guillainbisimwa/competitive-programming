def solve():
    n = int(input())
    last = [0] * (n + 1) 
    v = [[] for _ in range(n + 1)] 
    

    arr = list(map(int, input().split()))
    

    for i in range(1, n + 1):
        x = arr[i - 1] 
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            if x > last[m]:
                r = m - 1
            else:
                l = m + 1
        last[l] = x
        v[l].append(x)
    

    for i in range(1, n + 1):
        if v[i]: 
            print(' '.join(map(str, v[i]))) 

solve()
