class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        cnt = 0
        i = 0
        j = 0
        pro = 1
        while j < n:
            pro *= nums[j]
            while pro >= k and i <= j:
                pro /= nums[i]
                i += 1
            cnt += (j - i + 1)
            j += 1
        return cnt