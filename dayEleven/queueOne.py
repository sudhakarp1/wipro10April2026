class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.isEmpty():
            return 'Empty Queue'
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return 'Empty Queue'
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def disp(self):
        print(self.queue)

if __name__ == '__main__':
    myQueue = Queue()

    myQueue.disp()
    myQueue.enqueue(10)
    myQueue.enqueue(20)
    myQueue.enqueue(30)
    myQueue.enqueue(40)

    myQueue.disp()
    
    print(f'dequeued: {myQueue.dequeue()}')
    print(f'dequeued: {myQueue.dequeue()}')
    print(f'dequeued: {myQueue.dequeue()}')
    print(f'dequeued: {myQueue.dequeue()}')
    print(f'dequeued: {myQueue.dequeue()}')
