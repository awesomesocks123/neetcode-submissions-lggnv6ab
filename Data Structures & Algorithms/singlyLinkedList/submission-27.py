class ListNode:
    def __init__(self,val,next_node=None):
        self.val = val
        self.next = next_node 

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        count = 0
        cur = self.head.next 
        while cur:
            if count == index:
                return cur.val
            count += 1
            cur = cur.next 
        return -1 
        

    def insertHead(self, val: int) -> None:
        temp = ListNode(val)
        temp.next = self.head.next
        self.head.next = temp
        
        if not temp.next:
            self.tail = temp 

        

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next 

        

    def remove(self, index: int) -> bool:
        i = 0
        cur = self.head

        while i < index and cur:
            i += 1
            cur = cur.next
        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False 
        

    def getValues(self) -> List[int]:
        cur = self.head.next 
        res = [] 
        while cur:
            res.append(cur.val)
            cur = cur.next 
        return res 
        
