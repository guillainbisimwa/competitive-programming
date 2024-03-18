
# solution to problem D
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    pr_sum = [0] * (n + 1)
    
    for i in range(n):
        pr_sum[i + 1] = pr_sum[i] + arr[i]
    max_sum = 0
    
    for i in range(k + 1):
        current_max_sum = pr_sum[n - i] - pr_sum[2 * (k - i)]
        max_sum = max(max_sum, current_max_sum)
    print(max_sum)
