def max_operations(n, s):
    operations = 0
    i = 0
    while i < n - 1:
        if s[i] == 'A' and s[i + 1] == 'B':
            operations += 1
            i += 2  # Skip to avoid overlapping
        else:
            i += 1
    return operations

# Reading input
t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    results.append(max_operations(n, s))

# Output the results for each test case
print("\n".join(map(str, results)))
