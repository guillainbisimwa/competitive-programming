def findNumberOfOps(need, nums, n):
    ops=[0] * n 

    for i in range(n, 0, -1):
        num = i
        while num % 2 == 0:
            num /= 2 
            ops[i - 1] += 1
    
    ops.sort(reverse=True)
    ans = totSum = 0 
    for i, op in enumerate(ops):
        totSum += op 
        if totSum >= need:
            return i + 1 
    return -1
    
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    powers = 0 
    for num in nums:
        while num % 2 == 0:
            powers += 1
            num /= 2
    
    need = n - powers
    if need > 0:
        print(findNumberOfOps(need, nums, n))
    else:
        print(0)
