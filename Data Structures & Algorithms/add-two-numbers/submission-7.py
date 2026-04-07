# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 
        dummy = ListNode()
        current = dummy

        while l1 or l2:
            if l1:
                val1 = l1.val 
            else:
                val1 = 0
            if l2:
                val2 = l2.val 
            else:
                val2 = 0

            ans = val1 + val2 + carry
            carry = ans // 10 
            ans %= 10 
            current.next = ListNode(ans)
            
            if l1:
                l1 = l1.next

            if l2: 
                l2 = l2.next 
            current = current.next
        if carry:
            current.next = ListNode(carry)
        
        return dummy.next