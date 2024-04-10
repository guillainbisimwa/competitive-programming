class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        
        mn = [[nums[n - 1], n - 1] for _ in range(n)] 
        mx = [[nums[n - 1], n - 1] for _ in range(n)]
        
        for i in range(n - 2, -1, -1): 
            if nums[i] < mn[i + 1][0]:
                mn[i] = [nums[i], i]
            else:
                mn[i] = mn[i + 1]
            if nums[i] > mx[i + 1][0]:
                mx[i] = [nums[i], i]
            else:
                mx[i] = mx[i + 1]
        
        i = 0
        for j in range(n):
            if j - i < indexDifference:
                continue
            if abs(mn[j][0] - nums[i]) >= valueDifference:
                return [i, mn[j][1]]
            if abs(mx[j][0] - nums[i]) >= valueDifference:
                return [i, mx[j][1]]
            i += 1
        return [-1, -1]