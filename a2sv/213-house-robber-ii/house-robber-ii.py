class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        prevSkip, prevTake = 0, nums[0]
        prevSkip1, prevTake1 = 0, 0
        
        n = len(nums)
        
        for i in range(1, n):
            temp = max(prevSkip, prevTake)
            temp1 = max(prevSkip1, prevTake1)

            if i < n - 1:  
                prevTake = prevSkip + nums[i]
                prevSkip = temp

            prevTake1 = prevSkip1 + nums[i]  
            prevSkip1 = temp1
        
        return max(max(prevSkip, prevTake), max(prevSkip1, prevTake1))
