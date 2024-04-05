class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_line, max_row = float('-inf'), float('-inf')
        ans = 0
        while l < r:
            max_line = max(max_line, height[l])
            max_row = max(max_row, height[r])
            ans += (max_line < max_row) * (max_line - height[l]) + (max_row <= max_line) * (max_row - height[r])
            l += (max_line < max_row)
            r -= (max_row <= max_line)
        return ans
