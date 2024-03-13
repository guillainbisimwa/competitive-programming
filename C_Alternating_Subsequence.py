# def max_alternating_sum(arr, n):
#     max_sum = 0
#     # sign = "+" if arr[0] > 0 else "-"  
#     for i in range(n):  # Use n in the loop
#         if sign == "+" and arr[i] > 0:
#             j = i
#             current_max = 0
#             while j < n and arr[j] > 0:
#                 current_max = max(current_max, arr[j])
#                 j += 1
#             max_sum += current_max
#             sign = "-"
#             i = j - 1 

#         elif sign == "-" and arr[i] < 0:
#             j = i
#             current_max = float('-inf')
#             while j < n and arr[j] < 0:
#                 current_max = max(current_max, arr[j])
#                 j += 1
#             max_sum += current_max
#             sign = "+"
#             i = j - 1

#     return max_sum

# n = int(input())
# arr = list(map(int, input().split()))
# result = max_alternating_sum(arr, n)
# print(result)
