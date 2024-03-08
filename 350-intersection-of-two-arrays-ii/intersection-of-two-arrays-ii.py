class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        ans = []
        for num in nums1:
            count[num] = count.get(num, 0) + 1
            
        for num in nums2:
            if num in count and count[num] > 0:
                ans.append(num)
                count[num] -= 1
                
        return ans
