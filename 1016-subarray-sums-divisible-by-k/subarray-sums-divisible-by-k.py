class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ch = [0] * k
        ch[0] = 1
        sum_val = 0
        for i in range(n):
            sum_val += nums[i] % k + k
            ch[sum_val % k] += 1
        ans = 0
        for i in range(k):
            ans += (ch[i] * (ch[i] - 1)) // 2
        return ans