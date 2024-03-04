class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp1 = {}
        for num in arr1:
            if num in mp1:
                mp1[num] += 1
            else:
                mp1[num] = 1
        
        ans = []
        
        for num in arr2:
            ans.extend([num] * mp1[num])
            del mp1[num]
        
        remaining = []
        for num, count in mp1.items():
            remaining.extend([num] * count)
        
        remaining.sort()
        
        ans.extend(remaining)
        
        return ans