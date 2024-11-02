n = int(input())
box_sizes = list(map(int, input().split()))

box_sizes.sort()

count = {}
for size in box_sizes:
    if size in count:
        count[size] += 1
    else:
        count[size] = 1

max_ = max(count.values())

print(max_)
