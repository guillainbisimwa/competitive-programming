class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        count = 0
    
        minheap1 = []
        minheap2 = []   
        headptr = 0
        tailptr = len(costs) - 1
        
        while len(minheap1) < candidates and headptr <= tailptr:
            heapq.heappush(minheap1, costs[headptr])
            headptr += 1
        while len(minheap2) < candidates and headptr <= tailptr:
            heapq.heappush(minheap2, costs[tailptr])
            tailptr -= 1
        heapq.heapify(minheap1)
        heapq.heapify(minheap2)
        
        while k > 0:

            if minheap1 and minheap2:
                if minheap1[0] <= minheap2[0]:

                    count += heapq.heappop(minheap1)
                    if headptr <= tailptr and headptr < len(costs):
                        heapq.heappush(minheap1, costs[headptr])
                        headptr += 1
                else:
                    count += heapq.heappop(minheap2)
                    if headptr <= tailptr and tailptr >= 0:
                        heapq.heappush(minheap2, costs[tailptr])
                        tailptr -= 1
            elif not minheap1:
                count += heapq.heappop(minheap2)
            else:
                count += heapq.heappop(minheap1)
            
            k -= 1
        
        return count