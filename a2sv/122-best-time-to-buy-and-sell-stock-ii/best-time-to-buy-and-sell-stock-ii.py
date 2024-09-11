class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        max = 0

        length = len(prices)

        for i in range(0 , length):
            if start < prices[i]: 
                max += prices[i] - start
            start = prices[i]
        return max