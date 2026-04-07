class node:
    def __init__(self,val,next_node=None):
        self.val = val
        self.next = next_node 

class LinkedList:
    
    def __init__(self):
        self.head = node(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next 
        i = 0 
        while curr:
            if i == index:
                return curr.val
            i+=1
            curr = curr.next
        return - 1
        

    def insertHead(self, val: int) -> None:
        temp_node = node(val) 
        temp_node.next = self.head.next
        self.head.next = temp_node
        if not temp_node.next:
            self.tail = temp_node 
        

    def insertTail(self, val: int) -> None:
        self.tail.next = node(val)
        self.tail = self.tail.next 
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            #move curr to node before target node
            i += 1 
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False 

    def getValues(self) -> List[int]:
        curr = self.head.next
        valArr = []
        while curr:
            valArr.append(curr.val)
            curr = curr.next
        return valArr 
        
