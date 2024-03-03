def rearrange_array(n, arr):
    # Calculate the sum of the first and second halves of the array
    sum_first_half = sum(arr[:n])
    sum_second_half = sum(arr[n:])
    
    # Check if the sums are equal
    if sum_first_half == sum_second_half:
        return "-1"  # No solution
        
    # Sort the array to rearrange it
    arr.sort()
    
    # Output the rearranged array
    return " ".join(map(str, arr))

# Read input values
n = int(input())
arr = list(map(int, input().split()))

# Call the rearrange_array function and print the result
print(rearrange_array(n, arr))
