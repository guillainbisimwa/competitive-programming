import heapq

n, k = map(int, input().split())
songs = []

for _ in range(n):
    lengthElmnt, beuaty = map(int, input().split())
    songs.append((lengthElmnt, beuaty))

songs.sort(key=lambda x: x[1], reverse=True)

pq = []
ans = 0
length = 0

for lengthElmnt, beuaty in songs:
    if len(pq) == k:
        length -= heapq.heappop(pq)
    
    length += lengthElmnt
    heapq.heappush(pq, lengthElmnt)
    ans = max(ans, beuaty * length)

print(ans)