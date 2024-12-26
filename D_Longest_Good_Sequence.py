# import math
# n= int(input())
# a = list(map(int, input().split()))

# dp = [1] * n

# for i in range(1,n):
#     for j in range(i):
#         if math.gcd(a[i],a[j]) > 1:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))

size = input()
sequence = list(map(int, input().split()))
max_val = max(sequence) + 1
f_chain = [0] * max_val
factor_m = [[] for _ in range(max_val)]
factor_m[1] = [1]

for number in range(2, max_val):
    if not factor_m[number]:
        factor_m[number] = [number]
        for multiple in range(2 * number, max_val, number):
            factor_m[multiple].append(number)

for num in sequence:
    max_c = max(f_chain[factor] for factor in factor_m[num]) + 1
    for factor in factor_m[num]:
        f_chain[factor] = max_c

print(max(f_chain))
