import heapq
 
def main():
  """
  This function reads the number of test cases and processes each one to find the maximum total power.
  """
  t = int(input())
  for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))  # Read cards as integers
 
    max_heap = []  # Use heapq for max-heap
    min_heap = []  # Use heapq with custom comparison for min-heap
 
    for card in cards:
      if card > 0:
        heapq.heappush(max_heap, -card)  # Negate for max-heap behavior
      else:  # Hero card (card == 0)
        if max_heap:
          bonus_power = -heapq.heappop(max_heap)  # Retrieve and remove largest (negated smallest)
          heapq.heappush(min_heap, card + bonus_power)
        else:
          heapq.heappush(min_heap, card)
 
    total_power = 0
    while min_heap:
      total_power += heapq.heappop(min_heap)
 
    print(total_power)
 
if __name__ == "__main__":
  main()