class Solution:
    def check(self, i: int, cost: list[int], n: int, dp: dict[int, int]) -> int:

        if i >= n:
                return 0
        if i in dp:
            return dp[i]
        
        one = cost[i] + self.check(i + 1, cost, n, dp)
        two = cost[i] + self.check(i + 2, cost, n, dp)
        
        dp[i] = min(one, two)
        return dp[i]

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = {}
        
        start_from_0 = self.check(0, cost, n, dp)
        start_from_1 = self.check(1, cost, n, dp)
        
        return min(start_from_0, start_from_1)
        