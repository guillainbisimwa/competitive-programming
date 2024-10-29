def d(a, b, l):
    result = set()
    max_x, max_y = 0, 0
    temp_l = l
    
    while temp_l % a == 0:
        temp_l //= a
        max_x += 1
    
    # Reset temp_l
    temp_l = l
    
    while temp_l % b == 0:
        temp_l //= b
        max_y += 1
    
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            power_a = a ** x
            power_b = b ** y
            if (l % (power_a * power_b)) == 0:
                k = l // (power_a * power_b)
                result.add(k)
    
    return len(result)

t = int(input())
for _ in range(t):
    a, b, l = map(int, input().split())
    print(d(a, b, l))
