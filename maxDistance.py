class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 2

        if not q or len(q) == m * n:
            return -1
        x = 0 #init

        while q:
            q_next = []
            x += 1
            for v in q:
                r, c = v[0], v[1]

                if r - 1 >= 0 and grid[r - 1][c] == 0:
                    q_next.append((r - 1, c))
                    grid[r - 1][c] = 2
                if r + 1 < m and grid[r + 1][c] == 0:
                    q_next.append((r + 1, c))
                    grid[r + 1][c] = 2
                if c - 1 >= 0 and grid[r][c - 1] == 0:
                    q_next.append((r, c - 1))
                    grid[r][c - 1] = 2
                if c + 1 < n and grid[r][c + 1] == 0:
                    q_next.append((r, c + 1))
                    grid[r][c + 1] = 2
            q = q_next

        return x - 1
        