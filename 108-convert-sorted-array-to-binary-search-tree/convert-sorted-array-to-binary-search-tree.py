# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # nums is sorted
        n = len(nums)
        if n == 0:
            return
        
        middle = n // 2

        left = self.sortedArrayToBST(nums[:middle])
        right = self.sortedArrayToBST(nums[middle + 1:])
        node = TreeNode(nums[middle], left, right)
        return node
