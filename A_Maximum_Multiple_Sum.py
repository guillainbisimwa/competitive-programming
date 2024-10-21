def find_optimal_x(n):
    max_sum = 0
    best_x = 2
    
    for x in range(2, n+1):
        current_sum = sum(multiple for multiple in range(x, n+1, x))
        if current_sum > max_sum:
            max_sum = current_sum
            best_x = x
            
    return best_x

t = int(input())

for _ in range(t):
    n = int(input())
    print(find_optimal_x(n))
