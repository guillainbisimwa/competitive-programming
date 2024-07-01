n, target = map(int, input().split())
steps = list(map(int, input().split()))

current_position = 1

while current_position < target:
    if current_position == target:
        print("YES")
        break
    current_position += steps[current_position - 1]
else:
    print("YES" if current_position == target else "NO")
