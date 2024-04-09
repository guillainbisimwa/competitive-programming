class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j, sum_, min_length = 0, 0, 0, float('inf')

        while j < len(nums):
            sum_ += nums[j]

            while sum_ >= target:
                min_length = min(min_length, j - i + 1)
                sum_ -= nums[i]
                i += 1

            j += 1

        return min_length if min_length != float('inf') else 0