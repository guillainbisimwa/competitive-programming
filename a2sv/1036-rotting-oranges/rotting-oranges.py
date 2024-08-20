class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for _ in range(n)]
        q = deque()

        # init the queue with all rotten oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append(((i, j), 0))
                    visited[i][j] = 2

        maxtime = 0
        delx = [-1, 0, 1, 0]
        dely = [0, 1, 0, -1]

        # BFS
        while q:
            x, y = q[0][0]
            time = q[0][1]
            maxtime = max(maxtime, time)
            q.popleft()

            for i in range(4):
                row = x + delx[i]
                col = y + dely[i]
                if 0 <= row < n and 0 <= col < m and visited[row][col] != 2 and grid[row][col] == 1:
                    visited[row][col] = 2
                    q.append(((row, col), time + 1))

        # Check if there are any fresh oranges left
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] != 2:
                    return -1

        return maxtime
