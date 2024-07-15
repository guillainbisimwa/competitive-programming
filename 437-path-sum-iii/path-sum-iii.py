# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.Counter = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        if not root:
            return 0

        self.PathFromRoot(root, targetSum, 0)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)

        return self.Counter

    def PathFromRoot(self, root, target, Sum):
        if not root:
            return
        Sum += root.val

        if Sum == target:
            self.Counter += 1

        self.PathFromRoot(root.left, target, Sum)
        self.PathFromRoot(root.right, target, Sum)