class DynamicArray:
    
    def __init__(self, capacity: int):
        self._array = [0] * capacity
        self._capacity = capacity
        self._size = 0

    def get(self, i: int) -> int:
        return self._array[i]


    def set(self, i: int, n: int) -> None:
        self._array[i] = n

    def pushback(self, n: int) -> None:
        if self._size < self._capacity:
            self._array[self._size] = n
            self._size += 1
        else: 
            self.resize()
            self.pushback(n)

    def popback(self) -> int:
        self._size -= 1
        return self._array[self._size]

    def resize(self) -> None:
        t = self._array
        self._capacity *= 2
        self._array = [0] * self._capacity
        for i in range(self._size):
            self._array[i] = t[i]

    def getSize(self) -> int:
        return self._size
    
    def getCapacity(self) -> int:
        return self._capacity