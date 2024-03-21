class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        cnt = 0
        l = 0
        r = n - 1
        nums.sort()
        while l < r:
            if nums[l] + nums[r] == k:
                cnt += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
        return cnt
            