def find_start_index(n, k, heights):
    minimum = float('inf')
    index = 0
    
    current_sum = sum(heights[:k])
    minimum = current_sum
    
    for i in range(1, n - k + 1):
        current_sum = current_sum - heights[i - 1] + heights[i + k - 1]
        if current_sum < minimum:
            minimum = current_sum
            index = i
    
    return print(index + 1)

n, k = map(int, input().split())
heights = list(map(int, input().split()))
find_start_index(n, k, heights)

