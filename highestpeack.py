class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        ret = [[0] * n for _ in range(m)]
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = []

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append((i, j))
                    isWater[i][j] = -1
                    ret[i][j] = 0

        while len(q) > 0:
            current = q.pop(0)
            x = current[0]
            y = current[1]
            level = ret[x][y]

            for d in dir:
                xx = x + d[0]
                yy = y + d[1]

                if xx >= 0 and yy >= 0 and xx < m and yy < n:
                    if isWater[xx][yy] != -1:
                        isWater[xx][yy] = -1
                        q.append((xx, yy))
                        ret[xx][yy] = level + 1

        return ret
        