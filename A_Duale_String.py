def is_duale(s):
    if len(s) % 2 != 0:
        return "NO"
    
    half_length = len(s) // 2
    
    first_half = s[:half_length]
    second_half = s[half_length:]
    
    if first_half == second_half:
        return "YES"
    else:
        return "NO"

n = int(input())

for _ in range(n):
    s = input()

    result = is_duale(s)
    print(result)
