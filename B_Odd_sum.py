# Read input values
n = int(input())
arr = list(map(int, input().split()))

max_sum = sum(x for x in arr if x > 0)

# If max_sum is already odd, it's our answer
if max_sum % 2 != 0:
    print(max_sum)
else:
    smallest_odd_adjustment = float('inf')
    for x in arr:
        if abs(x) % 2 == 1:  # Chec
            smallest_odd_adjustment = min(smallest_odd_adjustment, abs(x))
    
    max_sum -= smallest_odd_adjustment
    print(max_sum)
