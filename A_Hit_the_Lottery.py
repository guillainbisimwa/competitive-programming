import heapq

def min_bills(n):
    dollars = n
    count = 0
    denominations = [-100, -20, -10, -5, -1]
    heapq.heapify(denominations) 

    while dollars > 0:
        largest = -heapq.heappop(denominations)
        if dollars >= largest:
            bills = dollars // largest
            count += bills
            dollars -= bills * largest

    return count

n = int(input())
print(min_bills(n))
