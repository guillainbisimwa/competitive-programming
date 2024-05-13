def sort(n, arr):
#   if a == 1:
#     return arr
#   arr = sort(a -1, arr)
#   arr[a-1], arr[a-2] =  arr[a-2], arr[a-1]
#   return arr

    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]