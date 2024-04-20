# Function to count the number of distinct non-empty strings
def count_distinct_strings(n, s):
    # Count the frequency of each character in the string
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Calculate the number of distinct non-empty strings
    distinct_strings = 0
    for char, count in freq.items():
        # Add the count of substrings of length 1
        distinct_strings += count
        
        # Add the count of substrings of length 2
        distinct_strings += count * (count - 1) // 2
    
    return distinct_strings

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the length of the string and the string itself
    n = int(input())
    s = input()
    
    # Count the number of distinct non-empty strings
    result = count_distinct_strings(n, s)
    
    # Output the result for the current test case
    print(result)
