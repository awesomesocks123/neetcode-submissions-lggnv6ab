class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0 
        self.cap = [0] * capacity


    def get(self, i: int) -> int:
        return self.cap[i]


    def set(self, i: int, n: int) -> None:
        self.cap[i] = n 


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.cap[self.size] = n
        self.size += 1


    def popback(self) -> int:
        self.size -= 1
        return self.cap[self.size] 

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        nwarr = [0] * self.capacity 

        for i in range(self.size):
            nwarr[i]  = self.cap[i]
        self.cap = nwarr


    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
