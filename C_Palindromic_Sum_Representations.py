def palindromic_sum_representations():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    queries = [int(data[i]) for i in range(1, t + 1)]
    max_n = max(queries)
    
    palindromes = []
    for i in range(1, max_n + 1):
        s = str(i)
        if s == s[::-1]: 
            palindromes.append(i)
    
    MOD = 10**9 + 7
    dp = [0] * (max_n + 1)
    dp[0] = 1 

    for p in palindromes:
        for j in range(p, max_n + 1):
            dp[j] = (dp[j] + dp[j - p]) % MOD

    results = [str(dp[n]) for n in queries]
    print("\n".join(results))

palindromic_sum_representations()