# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # n is 1 indexed 
        # do we have to reverse the list?

        #we can just run it via fast and slow but how? 

        #we can use two pointers

        #when the 2nd pointer reach the end we cycle thru the 2nd pointer to meet up with it so that it's always n places bhind
        # after we reach the current n 
        # we can just assign the prev.next == prev.next.next 
        #this way we can skip the current therefore removing it 

        #if n == 1: we can just return the list without its head 
        # head= head.next and then return 

        #set up a dummy
        dummy = ListNode(0,head) #handle edge case of removing head
        slow = dummy
        fast = head

        #move fast n steps ahead
        for i in range(n):
            fast = fast.next
        
        #now move both till we reach the end of the list
        while fast:
            slow = slow.next
            fast = fast.next
        #remove curr
        slow.next = slow.next.next
        return dummy.next 




