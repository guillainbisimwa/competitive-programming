class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # summ = sum(nums)
        # if summ % 2 == 1:
        #     return False
        
        # targetSum = summ // 2
        # n = [False] * (targetSum+1)        
        # n[0] = True
        
        # for num in nums:
        #     for j in range(targetSum, num-1, -1):
        #         n[j] = n[j] or n[j-num]
        
        # return n[targetSum]
        n = len(nums)
        memo = defaultdict(int)
        def dp(i, target_sum):
            if i >= n or target_sum <= 0:
                return target_sum == 0
            state = (i, target_sum)
            if state not in memo:
                memo[state] = dp(i + 1, target_sum - nums[i]) or\
                    dp(i + 1, target_sum)
            return memo[state]
        return sum(nums) % 2 == 0 and dp(0, sum(nums) // 2)