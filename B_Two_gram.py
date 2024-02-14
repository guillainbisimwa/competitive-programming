# Read input
n = int(input())
s = input()

max_count = 0
max_two_gram = ""

for i in range(n - 1):
    two_gram = s[i:i+2]
    
    count = s.count(two_gram)
    
    if count > max_count:
        max_count = count
        max_two_gram = two_gram

print(max_two_gram)
