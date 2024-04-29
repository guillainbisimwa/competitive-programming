n = int(input())
heights = list(map(int, input().split()))

heights.append(0)
stack = [-1]

maxLen = 0

for idx in range(n+1):
    cur = heights[idx]

    while stack and heights[stack[-1]] > cur:
        last = stack.pop()
        width = idx - stack[-1] -1
        height = heights[last]

        maxLen = max(maxLen, min(width, height))
    stack.append(idx)
print(maxLen)