def count_paths(distances, n, m):

  prefix_sums = [0] * len(distances)
  modulo_freq = {0: 1}  # Edge case: starting point (sum 0) is always valid

  for i in range(len(distances)):
    prefix_sums[i] = (prefix_sums[i - 1] + distances[i]) % m

  count = 0
  for num in prefix_sums:
    count += modulo_freq.get(num, 0)  
    modulo_freq[num] = modulo_freq.get(num, 0) + 1

  return count

n, m = map(int, input().split())
distance = list(map(int, input().split()))
result = count_paths(distance, n, m)
print(result)
