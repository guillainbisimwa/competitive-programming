"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        mapping = {}
        while temp:
            new_node = Node(temp.val)
            mapping[temp] = new_node
            temp = temp.next

        temp = head
        while temp:
            copied_node = mapping[temp]
            copied_node.next = mapping.get(temp.next)
            copied_node.random = mapping.get(temp.random)
            temp = temp.next

        return mapping.get(head)
