from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()

    def enqueueFront(self, data):
        self.deque.appendleft(data) 

    def enqueueRear(self, data):
        self.deque.append(data) 

    def dequeueFront(self):
        if self.isEmpty():
            return 'Empty Deque'
        return self.deque.popleft()
    
    def dequeueRear(self):
        if self.isEmpty():
            return 'Empty Deque'
        return self.deque.pop()
    
    def peak(self):
        if self.isEmpty():
            return None 
        return self.deque[0] 

    def isEmpty(self):
        return len(self.deque) == 0
    

if __name__ == '__main__':
    dqOne = Deque()

    dqOne.enqueueRear(10)
    dqOne.enqueueFront(60)
    dqOne.enqueueRear(100)
    dqOne.enqueueFront(5)

    while not dqOne.isEmpty():
        print(f'Popped: {dqOne.dequeueRear()}')
