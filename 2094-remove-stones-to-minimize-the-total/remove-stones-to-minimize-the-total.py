class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        
        for pile in piles:
            pile = -pile
            heap.append(pile)
        
        stones = sum(piles)
        
        heapq.heapify(heap)
        
        for _ in range(k):
            maxPile = heapq.heappop(heap)
            remove = (-maxPile) // 2

            stones -= remove
            heapq.heappush(heap, maxPile + remove)
        return stones
