'''
    Elements are dequeued based on priority
'''

import heapq 

class PriorityQueue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, data):
        heapq.heappush(self.queue, data)

    def dequeue(self):
        if self.isEmpty():
            return 'Empty Queue'
        return heapq.heappop(self.queue)
    
    def peek(self):
        if self.isEmpty():
            return 'Empty Queue'
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0

if __name__ == '__main__':
    queueOne = PriorityQueue()
    queueOne.enqueue(77) 
    queueOne.enqueue(88) 
    queueOne.enqueue(12)
    queueOne.enqueue(22)
    queueOne.enqueue(11)
    
    print(f'dequeued: {queueOne.dequeue()}')
    print(queueOne.enqueue(15));
    print(f'dequeued: {queueOne.dequeue()}')
    print(queueOne.enqueue(16))


