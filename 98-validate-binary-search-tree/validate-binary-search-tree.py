# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder_traversal(node, prev):
            if not node:
                return True
            if not inorder_traversal(node.left, prev):
                return False
            if node.val <= prev[0]:
                return False
            prev[0] = node.val
            return inorder_traversal(node.right, prev)

        # Start in-order traversal from the root node
        prev = [float('-inf')]  # Initialize previous value to negative infinity
        return inorder_traversal(root, prev)