from collections import Counter

def count_promising_subsegments(a, b, k):
  """
  Counts the number of promising subsegments in sequence 'a' given reference sequence 'b' and required matches 'k'.

  Args:
      a: The input sequence of integers.
      b: The reference sequence of integers.
      k: The required number of matches.

  Returns:
      The number of promising subsegments in sequence 'a'.
  """

  n = len(a)
  m = len(b)

  # Count frequencies of elements in both sequences
  a_counts = Counter(a)
  b_counts = Counter(b)

  # Count the number of elements in 'b' that have a frequency less than 'k' in 'a'
  non_promising_elements = 0
  for element, count in b_counts.items():
    if element not in a_counts or a_counts[element] < count:
      non_promising_elements += 1

  # Use sliding window to efficiently count promising subsegments
  count = 0  # Count of promising subsegments
  window_size = 0  # Size of the current window
  left = 0

  for right in range(n):
    # Add the current element to the window
    window_size += 1

    # Check if the current window can be promising
    if window_size >= m and (window_size - non_promising_elements) >= k:
      count += 1

    # Remove the leftmost element from the window if needed
    while left < right and window_size > m:
      if a[left] in b_counts:
        # Decrement the counter only if the element is from the reference sequence 'b'
        if a_counts[a[left]] <= b_counts[a[left]]:
          non_promising_elements -= 1
      a_counts[a[left]] -= 1
      left += 1
      window_size -= 1

  return count

def main():
  t = int(input())
  for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = count_promising_subsegments(a, b, k)
    print(count)

if __name__ == "__main__":
  main()
