class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        array = [0] * (2 * n)
        for i in range(n):
            array[2 * i] = nums[i]
            array[2 * i + 1] = nums[n + i]
        return array