def shortest_good_segment(n, s, nums):
    min_length = float('inf')
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += nums[right]

        while current_sum >= s:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else -1

# Input parsing
n, s = map(int, input().split())
nums = list(map(int, input().split()))

# Function call
result = shortest_good_segment(n, s, nums)

# Output
print(result)
