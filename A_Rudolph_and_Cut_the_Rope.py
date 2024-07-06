n = int(input().strip())

for _ in range(n):
    ropes = 0

    num_nails = int(input().strip())

    for _ in range(num_nails):
        a, b = map(int, input().strip().split())        
        if b < a:
            ropes += 1
    print(ropes)
