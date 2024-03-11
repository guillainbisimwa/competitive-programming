class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                res = nums[i] + nums[j]
                remaining = target - res
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    s = nums[left] + nums[right]
                    if s == remaining:
                        temp = [nums[i], nums[j], nums[left], nums[right]]
                        if temp not in ans:
                            ans.append(temp)
                        left += 1
                        right -= 1
                    elif s < remaining:
                        left += 1
                    else:
                        right -= 1
        return ans