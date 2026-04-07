class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0 
        self.arr = [0] * capacity #allocate populate with zeroes


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        #size check and resize
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n #insert 
        self.size += 1

    def popback(self) -> int:
        #decrement
        self.size -= 1
        return self.arr[self.size]
 

    def resize(self) -> None:
        self.capacity = 2 * self.capacity #double the capacity
        new_arr = [0] * self.capacity #temp array

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr #replaces temp with the original 

    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
