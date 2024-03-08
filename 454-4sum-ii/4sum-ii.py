class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        count = 0

        sum_map = {}

        for i in range(n):
            for j in range(n):
                somme = nums1[i] + nums2[j]
                sum_map[somme] = sum_map.get(somme, 0) + 1

        for k in range(n):
            for l in range(n):
                somme = -(nums3[k] + nums4[l])
                count += sum_map.get(somme, 0)

        return count