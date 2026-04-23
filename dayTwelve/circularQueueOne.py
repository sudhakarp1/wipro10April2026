'''
    Implementing Circular Queue using list as underlying DS
'''

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size 
        self.front, self.rear = -1, -1
    
    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            return 'Queue is full'
        if self.front == -1:
            self.front = 0 

        self.rear = (self.rear + 1) % self.size #
        self.queue[self.rear] = data  #Enqueue 
    
    def dequeue(self):
        if self.front == -1:
            return 'Empty Queue'
        
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size #

        return data 
    
    def isEmpty(self):
        return self.front == -1
    
    def peek(self):
        if self.front == -1:
            return None 
        return self.queue[self.front]
    
if __name__ == '__main__':
    queueOne = CircularQueue(5)
    queueOne.enqueue(10) ; print(f'front: {queueOne.front}   rear {queueOne.rear}')
    queueOne.enqueue(11); print(f'front: {queueOne.front}   rear {queueOne.rear}')
    queueOne.enqueue(12); print(f'front: {queueOne.front}   rear {queueOne.rear}')
    queueOne.enqueue(13); print(f'front: {queueOne.front}   rear {queueOne.rear}')
    queueOne.enqueue(14); print(f'front: {queueOne.front}   rear {queueOne.rear}')
    
    print(f'dequeued: {queueOne.dequeue()}')
    print(queueOne.enqueue(15)); print(f'front: {queueOne.front}   rear {queueOne.rear}')
    print(f'dequeued: {queueOne.dequeue()}')
    print(queueOne.enqueue(16)); print(f'front: {queueOne.front}   rear {queueOne.rear}')

