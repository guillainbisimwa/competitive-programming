class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        h = {}
        for num in nums:
            if num in h:
                h[num] = h[num] + 1
            else:
                h[num] = 1
        for key, value in h.items():
            if value > len(nums) / 3:
                l.append(key)
        return l
        