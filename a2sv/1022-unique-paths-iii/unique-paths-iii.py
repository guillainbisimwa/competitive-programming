class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        total = 0
        x = y = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1 and grid[i][j] != 2:
                    total += 1
                if grid[i][j] == 1:
                    x, y = i, j

        self.fonc(grid, total, 0, x, y)
        return self.ans
        
    def __init__(self):
        self.ans = 0

    def fonc(self, grid, total, x, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] == float('-inf'):
            return
        if grid[i][j] == 2:
            if x == total:
                self.ans += 1
            return
        if grid[i][j] == -1:
            return

        grid[i][j] = float('-inf')

        self.fonc(grid, total, x + 1, i + 1, j)
        self.fonc(grid, total, x + 1, i - 1, j)
        self.fonc(grid, total, x + 1, i, j + 1)
        self.fonc(grid, total, x + 1, i, j - 1)

        grid[i][j] = 0
