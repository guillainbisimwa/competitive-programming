class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prev_max = 0
        curr_max = 0

        for i in range(len(nums)):
            temp = curr_max  
            curr_max = max(curr_max, prev_max + nums[i]) 
            prev_max = temp 

        return curr_max 