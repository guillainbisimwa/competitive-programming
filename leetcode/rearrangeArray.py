class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        result = []
        i = 1
        length = len(nums)
        while i < length:
            result.append(sorted_nums[i])
            result.append(sorted_nums[i - 1])
            i += 2
        if length != len(result):
            result.append(sorted_nums[length - 1])
        return result