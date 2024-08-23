class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        questions.reverse()

        for i in range(n):
            if i > 0:
                dp[i] = max(dp[i], dp[i-1])
            
            if i - questions[i][1] - 1 < 0:
                dp[i] = max(dp[i], questions[i][0])
            else:
                dp[i] = max(dp[i], dp[i - questions[i][1] - 1] + questions[i][0])
        
        return dp[n-1]