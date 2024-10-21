class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_val = max_val = nums[0]
        
        for x in nums:
            if x > max_val:
                max_val = x
            elif x < min_val:
                min_val = x
        
        return self.gcd(max_val, min_val)
    def gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.gcd(b, a % b)

