t = int(input())

for _ in range(t):
    x = int(input())
    y = x & -x
    
    while True:
        if (x & y) > 0 and (x ^ y) > 0:
            print(y)
            break
        y += 1
