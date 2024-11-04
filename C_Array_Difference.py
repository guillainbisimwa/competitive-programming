def max_difference(n, m, a, b):
    # Sort the arrays
    a.sort()
    b.sort()
    
    # Calculate the maximum difference by pairing smallest with largest
    max_diff_1 = sum(abs(a[i] - b[i]) for i in range(n))
    # Calculate the maximum difference by pairing largest with smallest
    max_diff_2 = sum(abs(a[i] - b[m - n + i]) for i in range(n))
    
    # Return the maximum of both strategies
    return max(max_diff_1, max_diff_2)

# Reading input
t = int(input().strip())
results = []
for _ in range(t):
    n, m = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    results.append(max_difference(n, m, a, b))

# Output the results for each test case
print("\n".join(map(str, results)))
