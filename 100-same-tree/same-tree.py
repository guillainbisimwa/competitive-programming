# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        left_subtree_check = self.isSameTree(p.left, q.left)
        right_subtree_check = self.isSameTree(p.right, q.right)
        
        return p.val == q.val and left_subtree_check and right_subtree_check