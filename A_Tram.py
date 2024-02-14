n = int(input())

max_capacity = 0
current_capacity = 0

for _ in range(n):
    exiting, entering = map(int, input().split())
    
    current_capacity += entering - exiting
    
    max_capacity = max(max_capacity, current_capacity)

print(max_capacity)
