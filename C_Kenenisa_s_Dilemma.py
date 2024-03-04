def sort_array(n, arr):
    swaps = []
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            
            swaps.append((i, min_index))
    
    return sorted(swaps) 

n = int(input())
arr = list(map(int, input().split()))

swaps = sort_array(n, arr)

print(len(swaps))
for swap in swaps:
    print(swap[0], swap[1])

