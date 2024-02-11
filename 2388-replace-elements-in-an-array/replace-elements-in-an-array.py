class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = i
        for a in operations:
            mp[a[1]] = mp[a[0]]
            mp[a[0]] = -1
        for num, index in mp.items():
            if index >= 0:
                nums[index] = num
        return nums
        