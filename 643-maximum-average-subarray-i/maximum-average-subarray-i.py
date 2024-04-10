class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumCum = maxSum = sum(nums[:k])
        for i in range(k, len(nums)):

            sumCum += nums[i] - nums[i - k]
            
            maxSum = max(maxSum, sumCum)
        return maxSum / k