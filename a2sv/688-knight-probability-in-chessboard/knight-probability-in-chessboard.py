class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        xdir = [-2, -1, 2, 1, 1, 2, -1, -2]
        ydir = [1, 2, 1, 2, -2, -1, -2, -1]

        dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]

        def helper(moves, currR, currC):
            if moves == 0:
                return 1.0 if currR == row and currC == column else 0.0

            if dp[moves][currR][currC] != -1:
                return dp[moves][currR][currC]

            desiredOutcomes = 0.0
            totalOutcomes = 8.0

            for a in range(len(xdir)):
                x = currR + xdir[a]
                y = currC + ydir[a]
                if 0 <= x < n and 0 <= y < n:
                    desiredOutcomes += helper(moves - 1, x, y)

            dp[moves][currR][currC] = desiredOutcomes / totalOutcomes
            return dp[moves][currR][currC]

        ans = 0
        for i in range(n):
            for j in range(n):
                ans += helper(k, i, j)

        return ans
