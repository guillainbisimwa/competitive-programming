def min_operations_to_sort_string(s):
    # Check if the string is already sorted
    if s == ''.join(sorted(s)):
        return 0
    
    n = len(s)
    operations = 0
    sorted_s = ''.join(sorted(s))
    
    # Iteratively perform shifts on the lexicographically largest subsequence
    while s != sorted_s:
        # Find the lexicographically largest subsequence
        largest_char = max(s)
        largest_indices = [i for i, char in enumerate(s) if char == largest_char]
        
        # Check if impossible (no shifts can bring to sorted order)
        if all(s[i] == sorted_s[i] for i in range(n)):
            return -1
        
        # Pick the largest lexicographical subsequence
        for idx in largest_indices:
            if idx < n - 1:
                # Cyclically shift this subsequence
                s = s[:idx] + s[idx+1:] + s[idx]
                operations += 1
                break
        else:
            return -1  # No valid shifts left
    
    return operations

# Reading input
t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    results.append(min_operations_to_sort_string(s))

# Output the results for each test case
print("\n".join(map(str, results)))
