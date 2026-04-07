class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return  # Handle edge cases: empty list or single node

        # Step 1: Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        # Step 2: Reverse the second half of the list
        second_half = self.reverseList(mid.next)
        mid.next = None  # Disconnect the first half from the second half

        # Step 3: Merge the two halves
        first_half = head
        while second_half:  # Since second half might be shorter (for odd-length lists)
            temp1 = first_half.next
            temp2 = second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half = temp1
            second_half = temp2