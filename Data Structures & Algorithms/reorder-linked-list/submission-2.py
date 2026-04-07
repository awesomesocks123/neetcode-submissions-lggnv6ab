# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    
        #find middle
        if not head or not head.next:
            return

        slow, fast = head, head.next
        mid = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None #split list
        
        #reverse seodn half
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp 
        #merge the two half 
        l1 = head
        l2 = prev

        while l1 and l2:
            temp1 = l1.next
            temp2 = l2.next


            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2
        






