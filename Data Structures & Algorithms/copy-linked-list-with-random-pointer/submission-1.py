"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # original value val of the copied node
        # ListNode(curr.val)
        # the next pointer to the new node corespsond to the next pointer of the orignla nodde
        # newNode.next = curr.next
        #random pointer of the new node corresponds to the random pointer of the orignal node 


    #how do we keep track?
    # {3: next->7, random->null, 7:next->4, random->5, 4:next->5,random->3, 5:next->null,random->7, null}

    #we have to have a dictionary 
    #the key being the next
    #the value being the random 
    #when 7: 5
    
        oldToCopy = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]

