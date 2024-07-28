class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        for i, task in enumerate(tasks):
            heappush(heap, (task[0], task[1], i))

        order = []
        time = 0

        pt_heap = []
        while heap or pt_heap:
            while heap and heap[0][0] <= time:
                et, pt, i = heappop(heap)
                heappush(pt_heap, (pt, i))
            
            if pt_heap:
                pt, i = heappop(pt_heap)
                order.append(i)
                time += pt
            elif heap:
                time = heap[0][0]

        return order
