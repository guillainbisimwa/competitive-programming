class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #init stack [0,0,0,0]
        #stack = [0] * (len(arr))
        stk = [0] * (len(arr) + 1)
        idx = 0

        dp = [0] * len(arr)
        dp[0] = arr[0]

        res = dp[0]
        for i in range(1, len(arr)):
            while idx >= 0 and arr[stk[idx]] >= arr[i]:
                idx -= 1  # popping stack top

            dp[i] = arr[i] * (i + 1) if idx < 0 else dp[stk[idx]] + (arr[i] * (i - stk[idx]))
            res += dp[i]
            idx += 1
            stk[idx] = i  # pushing into stack

        return res % 1_000_000_007