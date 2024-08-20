class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # def
        #
        # if amount == 0:
        #     retrurn 1
         
        # dp =
        totAmout = amount + 1
        dp = [0] * (totAmout)
        dp[0] = 1
        
        for coin in coins:
            for j in range(coin, totAmout):
                dp[j] += dp[j - coin]
        
        return dp[totAmout - 1]