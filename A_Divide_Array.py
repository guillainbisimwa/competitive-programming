def divide_array(n, arr):
    part1, part2, part3 = [], [], []

    # Sort the array to easily divide it into partitions
    arr.sort()

    # Find the index of the first positive number (if any)
    first_positive_index = next((i for i, num in enumerate(arr) if num > 0), None)

    # Divide the array into partitions based on the first positive number
    if first_positive_index is not None:
        part1 = [arr[0]]
        part2 = arr[1:first_positive_index]
        part3 = arr[first_positive_index:]
    else:
        # If no positive number found, divide the array at the first zero
        first_zero_index = arr.index(0)
        part1 = arr[:first_zero_index]
        part2 = [arr[first_zero_index]]
        part3 = arr[first_zero_index + 1:]

    # Print the partitions
    print(len(part1), *part1)
    print(len(part2), *part2)
    print(len(part3), *part3)

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Call the function to divide the array into partitions
divide_array(n, arr)
