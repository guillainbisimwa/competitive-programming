class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        arr = [0] * (len(nums))

        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                i += 1
            i += 1

        j = 0
        k = 0
        while j < len(nums):
            if nums[j] != 0:
                arr[k] = int(nums[j])
                k += 1
            j += 1
        return list(arr)