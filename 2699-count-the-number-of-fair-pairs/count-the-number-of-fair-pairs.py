class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            x = self.l_bound(nums, i + 1, len(nums), lower - nums[i])
            y = self.u_bound(nums, i + 1, len(nums), upper - nums[i])
            ans += (y - x)
        return ans

    def l_bound(self, nums, start, end, target):
        left, right = start, end
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def u_bound(self, nums, start, end, target):
        left, right = start, end
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left