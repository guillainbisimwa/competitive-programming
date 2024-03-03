def sort_array(n, arr):
    swaps = []  # List to store the sequence of swaps
    
    for i in range(n):
        # Find the index of the minimum element from the current position to the end of the array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # If the minimum element is not at its correct position, swap it with the current element
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps.append((i, min_index))  # Add the swap to the list of swaps
    
    return swaps

# Read input values
n = int(input())
arr = list(map(int, input().split()))

# Call the sort_array function to find the sequence of swaps
swaps = sort_array(n, arr)

# Print the number of swaps and the sequence of swaps
print(len(swaps))
for swap in swaps:
    print(swap[0], swap[1])
