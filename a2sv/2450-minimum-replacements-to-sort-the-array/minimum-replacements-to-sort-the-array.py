class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        prev = nums[-1]
        
        for i in range(n - 2, -1, -1):
            if nums[i] > prev:
                parts = (nums[i] + prev - 1) // prev - 1
                result += parts
                prev = nums[i] // (parts + 1)
            else:
                prev = nums[i]
        
        return result