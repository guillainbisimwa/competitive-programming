class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n 

        res = 0
        maxi = 1

        for i in range(n):
            for prev in range(i):
                if nums[prev] < nums[i]:
                    if dp[prev] + 1 > dp[i]:
                        dp[i] = dp[prev] + 1
                        count[i] = count[prev]
                    elif dp[prev] + 1 == dp[i]:

                        count[i] += count[prev]
            maxi = max(maxi, dp[i])


        for i in range(n):
            if dp[i] == maxi:
                res += count[i]

        return res
