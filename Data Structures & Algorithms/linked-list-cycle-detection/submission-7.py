# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #set up slow and fast
        slow,fast = head, head.next
        #check for fast and fast.next so we dont get out of index and can return / run the while loop
        while fast and fast.next:
            if slow == fast:
                return True
            #cycle slow and fast 
            slow = slow.next
            #fast moves 2x faster
            fast = fast.next.next

        #return true when we run into a ==
        return False
        #return false after loop