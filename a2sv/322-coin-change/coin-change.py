class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
    
        dp[0] = 0

        for coin in coins:
            for current_amount in range(coin, amount + 1):
                dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]