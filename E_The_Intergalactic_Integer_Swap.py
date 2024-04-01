from math import gcd

def find_max_gcd(coordinates):

  n = len(coordinates)
  gcd_left = [0] * (n + 1)  

  # Calculate GCDs from the end, incorporating the padding element
  for i in range(n - 1, -1, -1):
    gcd_left[i] = gcd(gcd_left[i + 1], coordinates[i])

  max_gcd = float('-inf')
  running_gcd = 0

  # Calculate maximum GCD by combining elements from both sides
  for i in range(n):
    max_gcd = max(max_gcd, gcd(running_gcd, gcd_left[i + 1]))
    running_gcd = gcd(running_gcd, coordinates[i])

  return max_gcd

n = int(input())
coordinates = list(map(int, input().split()))

result = find_max_gcd(coordinates)
print(result)
