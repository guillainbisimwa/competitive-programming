class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(nums,key=lambda x:x / (10 ** len(str(x)) - 1 ), reverse=True)

        ans = ""
        for num in nums:
            ans += str(num)
        if ans[0] == '0':
            return "0"
        return ans