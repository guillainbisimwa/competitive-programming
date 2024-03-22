# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = [None] * 100
        ptr = head
        i = 0
        while ptr is not None:
            arr[i] = ptr
            i += 1
            ptr = ptr.next
        return arr[i // 2]