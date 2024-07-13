

# Read number of test cases
t = int(input())

# Main loop for each test case
while t > 0:
    t -= 1
    mini = float('inf')
    
    # Read number of elements in the array
    n = int(input())
    
    # Initialize the array
    a = [0] * (n + 1)
    
    # Read first element
    a[1] = int(input())
    
    # Loop through the remaining elements
    for i in range(2, n + 1):
        a[i] = int(input())
        mini = min(mini, max(a[i], a[i - 1]))
    
    # Decrement mini and print the result
    mini -= 1
    print(mini)
