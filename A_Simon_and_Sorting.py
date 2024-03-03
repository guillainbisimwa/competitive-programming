# Function to check if Simon can make the string abc with at most one swap
def simon_and_sorting(s):
    # Check if the string is already "abc" or "cba"
    if s == "abc" or s == "cba":
        return "YES"
    
    # Find the positions of a, b, and c in the string
    a_index = s.find('a')
    b_index = s.find('b')
    c_index = s.find('c')
    
    # Check if one swap is enough to make the string abc or cba
    if (a_index < b_index < c_index) or (c_index < b_index < a_index):
        return "YES"
    
    # Otherwise, return "NO"
    return "NO"

# List of strings to test
strings = ["abc", "acb", "bac", "bca", "cab", "cba"]

# Test each string
for s in strings:
    print(s, "->", simon_and_sorting(s))
