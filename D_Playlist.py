import heapq

n, k = map(int, input().split())
songs = []

for _ in range(n):
    first, second = map(int, input().split())
    songs.append((first, second))

songs.sort(key=lambda x: x[1], reverse=True)

pq = []
ans = 0
length = 0

for first, second in songs:
    if len(pq) == k:
        length -= heapq.heappop(pq)
    
    length += first
    heapq.heappush(pq, first)
    ans = max(ans, second * length)

print(ans)