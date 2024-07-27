def min_swaps_to_sort(arr):
    n = len(arr)
    arr_pos = [(arr[i], i) for i in range(n)]
    arr_pos.sort()

    visited = [False] * n
    
    swaps = 0

    for i in range(n):
        if visited[i] or arr_pos[i][1] == i:
            continue
        
        cycle_size = 0
        j = i

        while not visited[j]:
            visited[j] = True
            j = arr_pos[j][1]
            cycle_size += 1
        
        if cycle_size > 0:
            swaps += (cycle_size - 1)

    return swaps-1

n = int(input())
weights = list(map(int, input().split()))

print(min_swaps_to_sort(weights))
