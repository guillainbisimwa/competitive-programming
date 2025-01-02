# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        path_nodes = []
        
        self.find_path(root, target, path_nodes)
        
        for i in range(len(path_nodes)):
            self.k_level(path_nodes[i], k - i, ans, None if i == 0 else path_nodes[i - 1])
        
        return ans

    def k_level(self, root: Optional[TreeNode], k: int, ans: List[int], blocker: Optional[TreeNode]):
        if root is None or k < 0 or root == blocker:
            return
        if k == 0:
            ans.append(root.val)
            return

        self.k_level(root.left, k - 1, ans, blocker)
        self.k_level(root.right, k - 1, ans, blocker)

    def find_path(self, root: Optional[TreeNode], target: TreeNode, ans: List[TreeNode]) -> bool:
        if root is None:
            return False
        if root == target:
            ans.append(root)
            return True

        #  left 
        left_found = self.find_path(root.left, target, ans)
        if left_found:
            ans.append(root)
            return True

        right_found = self.find_path(root.right, target, ans)
        if right_found:
            ans.append(root)
            return True

        return False