# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        fastPointer = head.next
        slowPointer = head

        while fastPointer and fastPointer.next:
            if fastPointer.val == slowPointer.val:
                return True
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
        return False