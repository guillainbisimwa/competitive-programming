# Read input
n, k = map(int, input().split())
sequence = list(map(int, input().split()))

# Sort the sequence
sequence.sort()

# If k is 0, print the smallest element in the sequence
if k == 0:
    print(sequence[0] - 1 if sequence[0] > 1 else -1)
    exit()

# If k is equal to n, print the largest element in the sequence
if k == n:
    print(sequence[-1])
    exit()

# Find the k-th element in the sorted sequence
x = sequence[k - 1]

# Find the last index of x in the sorted sequence
last_index = sequence.index(x, k - 1)

# If there are more than k elements equal to x, decrease x by 1
if last_index - (k - 1) > 1:
    x -= 1

# Print the value of x
print(x)
