# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head



        slowP = dummy
        fastP = dummy
        count = 0
        for _ in range(n + 1):
            fastP = fastP.next
            count +=1
        if count == 1:
            return dummy

        if count == n:
            return head.next

        while fastP:
            fastP = fastP.next
            slowP = slowP.next
            
        slowP.next = slowP.next.next

        return dummy.next






