def cut():
    n = int(input())
    a = list(map(int, input().split()))
    b = a.copy()
    a.sort()
    for i in range(n):
        if a[i] % 2 != b[i] % 2:
            return "NO"
 
    return "YES"

t = int(input())
while t > 0:
    print(cut())
    t -= 1

 