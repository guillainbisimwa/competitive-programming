class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1]*n]*m
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c]:
                        dp[r][c] = 0
                        continue
                
                if r>0 or c>0:
                    if r>0 and c>0:
                        dp[r][c] = dp[r-1][c] + dp[r][c-1]
                    elif r>0:
                        dp[r][c] = dp[r-1][c]
                    else:
                        dp[r][c] = dp[r][c-1]
                else:
                    dp[r][c] = 1
        return dp[m-1][n-1]