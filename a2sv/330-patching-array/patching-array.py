class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        sum_ = 0
        cnt = 0
        i = 0

        while sum_ < n:
            if i < len(nums) and nums[i] <= sum_ + 1:
                sum_ += nums[i]
                i += 1
            else:
                cnt += 1
                sum_ = sum_ * 2 + 1

        return cnt