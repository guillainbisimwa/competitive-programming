class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor_sum = 0
        
        # XOR all the numbers in nums
        for num in nums:
            xor_sum ^= num
        
        # XOR the result with all numbers from 0 to n
        for i in range(n + 1):
            xor_sum ^= i
        
        return xor_sum
        