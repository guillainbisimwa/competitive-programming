def process_test_cases():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ar = list(map(int, input().split()))

        # Check if all elements are the same
        if len(set(ar)) == 1:
            print("NO")
        else:
            # Sort the array in descending order
            ar.sort(reverse=True)
            
            # If the first two elements are the same, swap the second with the last element
            if ar[0] == ar[1]:
                ar[1], ar[-1] = ar[-1], ar[1]
            
            print("YES")
            # Print the array as a space-separated string
            print(" ".join(map(str, ar)))
            print(" ".join(map(str, sorted(ar, reverse=True))))


# Call the function to process test cases
process_test_cases()
