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
        current = head
        current_map = {}
        current_map[None] = None
        while current:
            temp = Node(current.val)
            current_map[current] = temp
            current = current.next
        current = head
        while current:
            temp = current_map[current]
            temp.next = current_map[current.next]
            temp.random = current_map[current.random]
            current = current.next
        return current_map[head]