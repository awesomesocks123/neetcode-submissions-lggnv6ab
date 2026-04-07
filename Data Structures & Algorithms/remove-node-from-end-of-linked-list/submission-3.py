# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        head = [1,2,3,4] n = 2
        indx ele
        0     1
        1     2
        2     3
        3     4

        remove 2
        [1,2,4] 

        we can use a counter
        i = 0 

        as we traverse once we hit one before i 
        we set the i next to i next.next

        1 -> 2 -> 3 -> 4
        0    1
             | 
            curr
                 curr.next = 3
                    curr.next.next = 4
            if i = n - 1
                curr.next = curr.next.next 
        from end of linked list?
        not sure how this make sense?

        """
        dummy = ListNode(0)
        dummy.next = head

        slowp,fastp = dummy, dummy
        count = 0
        for _ in range(n + 1):
            fastp = fastp.next
            count += 1
        
        while fastp:
            fastp = fastp.next
            slowp = slowp.next
        slowp.next = slowp.next.next
        return dummy.next 









