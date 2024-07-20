t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    res = "YES"
    for i in range(1, n):
        if a[i] - a[i - 1] > 1:
            res = "NO"
            break 
    
    print(res) 