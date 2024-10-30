class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1] * (len(t) + 1) for _ in range(len(s) + 1)]
        
        def solve(currentInd, currentTarIn):
            if currentTarIn >= len(t):  # Target string t is fully matched
                return 1
            if currentInd >= len(s):  # Source string s is exhausted
                return 0
            if dp[currentInd][currentTarIn] != -1:  # Use cached result
                return dp[currentInd][currentTarIn]
            
            # Skip current character of s and solve for next
            res = solve(currentInd + 1, currentTarIn)
            
            # If characters match, add result of including current character
            if s[currentInd] == t[currentTarIn]:
                res += solve(currentInd + 1, currentTarIn + 1)
            
            # Store result in dp table
            dp[currentInd][currentTarIn] = res
            return res
        
        return solve(0, 0)
