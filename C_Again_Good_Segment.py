def find_non_mod_subarrays(n, k, x):
 
  ans = n * (n + 1) // 2
  j = 0
  cnt = {}

  for i in range(n):
    while j < n and cnt.get(x[j], 0) + 1 < k:
      cnt[x[j]] = cnt.get(x[j], 0) + 1  
      j += 1

    ans -= j - i

    cnt[x[i]] = cnt.get(x[i], 0) - 1

  return ans

n, k = map(int, input().split())

x = tuple(map(int, input().split()))

result = find_non_mod_subarrays(n, k, x)
print(result)
