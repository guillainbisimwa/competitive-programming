class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_val = float('inf')
        max_val = float('-inf')

        for n in nums:
            min_val = min(min_val, n)
            max_val = max(max_val, n)

        counting = [0] * (max_val - min_val + 1)

        for n in nums:
            counting[n - min_val] += 1

        i = 0
        for j in range(len(counting)):
            freq = counting[j]
            while freq != 0:
                nums[i] = j + min_val
                i += 1
                freq -= 1

        return nums