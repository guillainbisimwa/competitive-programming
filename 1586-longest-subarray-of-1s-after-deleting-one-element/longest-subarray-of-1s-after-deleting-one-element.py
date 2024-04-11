class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        v = [-1]
        for i in range(len(nums)):
            if nums[i] == 0:
                v.append(i)
        v.append(len(nums))

        m = 0
        for i in range(1, len(v) - 1):
            m = max(m, v[i + 1] - v[i - 1] - 2)

        if len(v) == 2:
            return len(nums) - 1

        return m