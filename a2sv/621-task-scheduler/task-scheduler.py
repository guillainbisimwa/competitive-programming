class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = {}
        for task in tasks:
            if task in task_count:
                task_count[task] += 1
            else:
                task_count[task] = 1
        
        max_heap = []
        for count in task_count.values():
            heapq.heappush(max_heap, -count)  
        ans = 0
        while max_heap:
            temp = []
            time = 0
            
            for _ in range(n + 1):
                if max_heap:
                    current_count = -heapq.heappop(max_heap) - 1  # Decrease the count
                    if current_count > 0:
                        temp.append(-current_count)  # Store the remaining count
                    time += 1
            
            for count in temp:
                heapq.heappush(max_heap, count)
            
            if max_heap:
                ans += n + 1
            else:
                ans += time
        
        return ans