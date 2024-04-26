class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if not nums1 or not nums2:
            return [] 

        m = {} 
        stack = []  

        for num in nums2[::-1]: ## reverse order??
            while stack and stack[-1] <= num:
                stack.pop() 
            next_greater = stack[-1] if stack else -1
            m[num] = next_greater
            stack.append(num)

        
        return [m.get(num, -1) for num in nums1] 
        # Return the next greater element for each element in nums1 (or -1 if not found)??

