# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.map = defaultdict(lambda: defaultdict(list))

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dfs(root, 0, 0)
        result = []

        for x in sorted(self.map.keys()):
            nums = []
            # Sort the y within each x and gather the values
            for y in sorted(self.map[x].keys()):
                values = sorted(self.map[x][y])
                nums.extend(values)
            result.append(nums)

        return result
    def dfs(self, root: Optional[TreeNode], x: int, y: int):
        if not root:
            return
        
        self.map[x][y].append(root.val)
        
        # Traverse l and r 
        self.dfs(root.left, x - 1, y + 1)
        self.dfs(root.right, x + 1, y + 1)