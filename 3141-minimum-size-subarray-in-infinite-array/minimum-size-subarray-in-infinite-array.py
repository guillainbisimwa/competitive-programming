class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:

        if target == 0:
            return 0

        total = sum(nums)
        if target >= total:
            quotient = target // total
            remainder = target % total
            sub_result = self.minSizeSubarray(nums, remainder)
            if sub_result == -1:
                return -1
            return len(nums) * quotient + sub_result

        min_len = float('inf')
        current_sum = 0
        left, right = 0, 0

        while right < 2 * len(nums):
            current_sum += nums[right % len(nums)]

            while left < right and current_sum > target:
                current_sum -= nums[left % len(nums)]
                left += 1

            if current_sum == target:
                min_len = min(min_len, right - left + 1)

            right += 1

        return min_len if min_len != float('inf') else -1