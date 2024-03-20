def count_good_segments(n, s, nums):
    count = 0
    prefix_sum = 0
    j = 0
    
    for i in range(n):
        prefix_sum += nums[i]
        
        while prefix_sum > s:
            prefix_sum -= nums[j]
            j += 1
        
        count += (i - j + 1)
    
    return count

if __name__ == "__main__":
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    
    result = count_good_segments(n, s, nums)
    print(result)