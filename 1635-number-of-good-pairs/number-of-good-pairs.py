class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        occurrences = [0] * 101

        for num in nums:
            count += occurrences[num]
            occurrences[num] += 1

        return count
