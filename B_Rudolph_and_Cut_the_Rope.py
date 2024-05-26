n = int(input())
 
for _ in range(n):
    v, n = int(input()), 0
    # n = 0
    for _ in range(v):
        current  = input().split()

        if(int(current [1]) < int(current [0])):
            n += 1
    
    print(n)