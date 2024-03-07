class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for item in nums:
            if i < 2 or nums[i - 2] != item:
                nums[i] = item
                i += 1
        return i