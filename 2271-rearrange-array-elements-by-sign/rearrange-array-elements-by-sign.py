class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [None] * len(nums)
        posPointer = 0
        negPointer = 1

        for element in nums:
            if element > 0:
                result[posPointer] = element
                posPointer += 2
            else:
                result[negPointer] = element
                negPointer += 2

        return result
            