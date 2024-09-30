class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        ans_zero = ans_two = 0
        ans_one = -prices[0]

        for index in range(1, len(prices)):
            temp = ans_two
            ans_two = ans_one + prices[index]
            ans_one = max(ans_zero - prices[index], ans_one)
            ans_zero = max(ans_zero, temp)

        return max(ans_zero, ans_two)