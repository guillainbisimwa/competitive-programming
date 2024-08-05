class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        charhe = []
        for i in range(len(quality)):
            ratio = wage[i] / quality[i]
            charhe.append((ratio, quality[i]))
        
        # Sort the list based on the wage to quality ratio
        charhe.sort()
        
        ans = float('inf')
        total_quality = 0
        workers_count = 0
        heap = []
        
        # Iterate through the sorted list
        for ratio, q in charhe:
            total_quality += q
            workers_count += 1
            heappush(heap, -q)
            
            if workers_count < k:
                continue
            
            while workers_count > k:
                total_quality += heappop(heap)
                workers_count -= 1
            
            current_cost = total_quality * ratio
            ans = min(ans, current_cost)
        
        return ans