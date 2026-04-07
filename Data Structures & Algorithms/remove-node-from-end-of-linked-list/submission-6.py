class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev  

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Thought Process for removing the Nth node from the end.

        Example: head = [1, 2, 3, 4], n = 2
        
        Index | Element
        ----------------
          0   |    1
          1   |    2
          2   |    3
          3   |    4

        Target: Remove the 2nd node from the end (node with value 3).
        Expected Result: [1, 2, 4]

        Initial Idea:
        - The challenge is identifying the node from the "end" of the list
          when we can only traverse from the "beginning."

        Proposed Algorithm (Multi-pass):
        1. Reverse the linked list. This turns the problem into
           "remove the Nth node from the beginning."
        2. Traverse the new, reversed list and remove the Nth node.
        3. Reverse the list back to its original order.
        4. Return the head of the modified list.
        """

        # Step 1: Reverse the list while attempting to find the deletion spot.
        reversedhead = self.reverse(head)
        if n == 1:
            reversedhead = reversedhead.next
            return self.reverse(reversedhead)


        count = 1
        curr = reversedhead
        #draw this out 
        while count < n - 1:
            curr = curr.next
            count += 1
        if curr and curr.next:
            curr.next = curr.next.next
        return self.reverse(reversedhead)
    











