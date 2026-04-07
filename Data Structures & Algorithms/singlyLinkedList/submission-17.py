class Node:
    def __init__(self,value, next_node=None):
        self.value = value
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        i = 0 
        current = self.head.next
        while current:
            if i == index:
                return current.value
            i += 1
            current = current.next
        return -1
        

    def insertHead(self, val: int) -> None:
        temp = Node(val)
        temp.next = self.head.next
        self.head.next = temp
        if not temp.next:
            self.tail = temp

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

        

    def remove(self, index: int) -> bool:
        i = 0 
        current = self.head

        while i < index and current.next is not None:
            current = current.next
            i += 1
        if current.next is None:
            return False
        target = current.next
        current.next = target.next
        if target == self.tail:
            self.tail = current
        return True
        

    def getValues(self) -> List[int]:
        res = []
        current = self.head.next 
        while current:
            res.append(current.value)
            current = current.next
        return res
        
