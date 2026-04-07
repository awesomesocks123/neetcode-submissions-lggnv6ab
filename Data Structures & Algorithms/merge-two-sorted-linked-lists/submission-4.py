# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # we have to create a new list?
        
        #iterate thru both

        #whatever is left over append it to the curr

        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                #set curr.next to the curr listnode
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            #cycle curr
            curr = curr.next
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        return dummy.next
        #return dummy? 