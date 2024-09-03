class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for i in range(32):
            sum_bits = 0
            for num in nums:
                sum_bits += (num >> i) & 1
            sum_bits %= 3
            ans |= (sum_bits << i)

        if ans >= 2 ** 31:
            ans -= 2 ** 32

        return ans