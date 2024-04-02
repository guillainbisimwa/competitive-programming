class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot = 1
        count = 0
        
        for num in nums:
            if num != 0:
                tot *= num
            else:
                count += 1
                
        result = []
        
        if count > 1:
            return [0] * len(nums)
        
        for num in nums:
            if num != 0:
                if count == 1:
                    result.append(0)
                else:
                    result.append(tot // num)
            else:
                result.append(tot)
        
        return result