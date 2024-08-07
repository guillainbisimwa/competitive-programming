class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        
        def dp(m):
            if m == 0: 
                return 0
            if m == 1 or m == 2: 
                return 1

            if m not in memo:
                memo[m] = dp(m - 1) + dp(m - 2) + dp(m - 3)

            return memo[m]
        return dp(n)