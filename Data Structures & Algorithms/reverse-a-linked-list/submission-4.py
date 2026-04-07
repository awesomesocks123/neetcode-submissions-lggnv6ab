# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #create a prev to keep track
        #start cycling using curr

        prev, curr = None, head

        while curr:
            #temp to hold next value as we do reassignment

            temp = curr.next

            curr.next = prev

            prev = curr

            curr = temp
        
        return prev