# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            cur = TreeNode(num)
            while stack and stack[-1].val < num:
                cur.left = stack.pop()
            if stack:
                stack[-1].right = cur
            stack.append(cur)
        return stack[0]  # Return the first element in the stack