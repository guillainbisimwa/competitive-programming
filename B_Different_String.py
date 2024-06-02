t = int(input())
 
 
for _ in range(t):
    a = input()
    r = len(set(a))
    if r == 1:
        print("NO")
    else:
        print("YES")
        x = a[-1] + a[:-1]
        print(x)

        
 