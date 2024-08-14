class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D lis
        a = [[0] * n for _ in range(m)]
        return self.dest(a, m, n, 0, 0)

    def dest(self, a: list, m: int, n: int, i: int, j: int) -> int:
        if i >= m or j >= n:
            return 0
        
        if i == m - 1 and j == n - 1:
            return 1
        
        if a[i][j] > 0:
            return a[i][j]
        
        a[i][j] = self.dest(a, m, n, i + 1, j) + self.dest(a, m, n, i, j + 1)
        return a[i][j]