def segment_with_small_sum(arr, s):
   n = len(arr)
   left, right, current_sum, max_length = 0, 0, 0, 0

   while right < n:
       current_sum += arr[right]

       while current_sum > s and left <= right:
           current_sum -= arr[left]
           left += 1

       max_length = max(max_length, right - left + 1)

       right += 1 
   return max_length

n, s = map(int, input().split())
arr = list(map(int, input().split()))
result = segment_with_small_sum(arr, s)
print(result)
