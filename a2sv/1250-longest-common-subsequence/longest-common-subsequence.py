class Solution:
    def lcs(self, x: str, y: str, n: int, m: int) -> int:
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill the dp array
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if x[i - 1] == y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The answer is in dp[n][m]
        return dp[n][m]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.lcs(text1, text2, len(text1), len(text2))