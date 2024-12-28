class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetFreq = [0] * n
        
        meetings.sort()

        pq = []
        available = set(range(n))  # Set of available rooms

        for meeting in meetings:
            start, end = meeting
            
            while pq and pq[0][0] <= start:
                _, room_id = heapq.heappop(pq)
                available.add(room_id)

            if available:
                room_id = min(available)
                meetFreq[room_id] += 1
                heapq.heappush(pq, (end, room_id))
                available.remove(room_id)
            else:
                end_time, room_id = heapq.heappop(pq)
                new_end = end_time + (end - start)
                meetFreq[room_id] += 1
                heapq.heappush(pq, (new_end, room_id))

        # Find the room with the maximum frequency
        max_meetings = -1
        result = -1
        for room_id in range(n):
            if meetFreq[room_id] > max_meetings:
                max_meetings = meetFreq[room_id]
                result = room_id
        
        return result