# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        myList = ListNode()
        
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i, lists[i]))
        
        current = myList
        while heap:
            value, i, node = heappop(heap)
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
            
            current.next = node
            current = node
        
        return myList.next