import heapq

def total_rooms_needed(n, experiments):
    events = []
    for s, t, b in experiments:
        events.append((s, b))
        events.append((t + 1, -b))

    events.sort()

    current_rooms = 0
    max_rooms = 0
    min_heap = []

    for time, rooms in events:
        current_rooms += rooms
        if rooms > 0:
            heapq.heappush(min_heap, (time, rooms))
        else:
            while min_heap and min_heap[0][0] < time:
                heapq.heappop(min_heap)
        
        max_rooms = max(max_rooms, current_rooms)

    return max_rooms

n = int(input())
experiments = [tuple(map(int, input().split())) for _ in range(n)]

print(total_rooms_needed(n, experiments))
