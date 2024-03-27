def min_substring_length(n, s):
    k = len(set(s))
    leng = 0
    obValues = {}
    ans = n
    
    for r in range(n):
        obValues[s[r]] = obValues.get(s[r], 0) + 1

        while len(obValues) >= k:
            ans = min(ans, r - leng + 1)
            obValues[s[leng]] -= 1
            if obValues[s[leng]] == 0:
                del obValues[s[leng]] 
            leng += 1
    
    return ans

n = int(input())
s = input()

print(min_substring_length(n, s))
