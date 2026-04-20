'''
    Imlementing Dynamic array
        ctypes module:
            can use c library ...
            Is used to bridge between C and Python     
            py_object() --> returns python object to be used in Python
'''
import ctypes

class DynamicArray:
    def __init__(self): #constructor
        self._size = 0 
        self._capacity = 1
        self._Array = self._makeArray(self._capacity)

    def __len__(self): #len()
        return self._size
    
    def capacity(self):
        return self._capacity

    def __getitem__(self, key): #[] operator
        if not 0 <= key < self._size:
            raise IndexError(f'Invalide Index: {key}')
        return self._Array[key]        

    def append(self, value):
        if self._size == self._capacity:
            #print(f'Resizing... {self._size}')
            self._resize(2 * self._capacity)
        self._Array[self._size] = value
        self._size += 1

    def _resize(self, cap):
        tempArray = self._makeArray(cap) 
        for i in range(self._size):
            tempArray[i] = self._Array[i]
        self._Array = tempArray
        self._capacity = cap

    def insert(self, pos, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        
        for i in range(self._size, pos, -1):
            self._Array[i] = self._Array[i - 1]

        self._Array[pos] = value
        self._size += 1

    def remove(self, value):
        for key in range(self._size):
            if self._Array[key] == value:
                for j in range(key, self._size - 1):
                    self._Array[j] = self._Array[j+1]   
                self._Array[self._size - 1] = None
                self._size -= 1
                return
        raise ValueError('value not found')
    
    def _makeArray(self, cap):
        #return new array of given capacity
        return (cap * ctypes.py_object)() 

    def __str__(self):
        tempLst = [self._Array[i] for i in range(self._size)]
        return f'Dynamic Array: {tempLst}'
        
if __name__ == '__main__':
    arrOne = DynamicArray()
    for i in range(10):
        #a = len(arrOne)
        #print(f'Length: {a}  capacity: {arrOne.capacity()}')
        arrOne.append(100 + i)

    print(arrOne)
    arrOne.remove(105)
    print(arrOne)