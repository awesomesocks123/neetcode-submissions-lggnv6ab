class Node:
    def __init__(self,val,next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1) #dummy head 
        self.tail = self.head

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next # next points to the data
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1
        

    def insertHead(self, val: int) -> None:
        temp = Node(val)
        temp.next = self.head.next
        self.head.next = temp 
        if temp.next is None:
            self.tail = temp

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next 
        
    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head #dummy head 
        while i < index and curr.next is not None:
            curr = curr.next
            i += 1
        if curr.next is None:
            return False 
        target = curr.next
        curr.next = target.next 

        if target.next is None:
            self.tail = curr
        return True
        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr: 
            res.append(curr.val)
            curr = curr.next
        return res
        
