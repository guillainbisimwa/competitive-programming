import heapq
n = int(input())
l = list(map(int, input().split()))
q = []
sm = 0
for el in l:
    sm += el
    heapq.heappush(q, el)
    while sm < 0:
        sm -= heapq.heappop(q)
print(len(q))
