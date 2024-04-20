def count_beautiful_pairs(n, x, y, a):
    beautiful_pairs = 0
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % x == 0 and a[j] % y == 0:
                beautiful_pairs += 1
    
    return beautiful_pairs

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the inputs
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Calculate the number of beautiful pairs
    result = count_beautiful_pairs(n, x, y, a)
    
    # Output the result for the current test case
    print(result)
