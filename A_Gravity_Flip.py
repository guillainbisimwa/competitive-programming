n = int(input())  # nbr of elements
numbers = list(map(int, input().split()))
numbers.sort()

print(' '.join(map(str, numbers)))
