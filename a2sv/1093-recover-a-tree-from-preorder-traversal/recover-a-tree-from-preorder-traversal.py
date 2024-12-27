# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ind = 0
        self.s = ""

    def solve(self, depth):
        if len(self.s) < depth:
            return None

        for i in range(self.ind, self.ind + depth):
            if i >= len(self.s) or self.s[i] != '-':
                return None

        temp = ""
        st = self.ind + depth
        while st < len(self.s) and self.s[st] != '-':
            temp += self.s[st]
            st += 1

        value = int(temp)
        root = TreeNode(value)
        self.ind = st
        root.left = self.solve(depth + 1)
        root.right = self.solve(depth + 1)
        return root

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        self.s = traversal  # Correct variable name
        return self.solve(0)
