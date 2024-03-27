class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        length = 1
        
        while left < len(nums) and right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[left + 1] = nums[right]
                left += 1
                length += 1
        
        return length
        