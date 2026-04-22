'''
    stacks implementation :
        with Linked List as underlying data structure
'''

class Node:
    def __init__(self, data):
        self.data, self.next = data, None
    
    def __str__(self):
        return f'data: {self.data} Next: {self.next}'

class Stack:
    def __init__(self):
        self.top = None 

    def Push(self, data):
        newNode = Node(data)
        newNode.next = self.top 
        self.top = newNode

    def Pop(self):
        if self.isEmpty(): 
            return 'Empty List'
        
        temp = self.top 
        self.top = self.top.next
        return temp.data
    
    def isEmpty(self):
        return self.top is None
    
    def Peek(self):
        if self.isEmpty(): 
            return 'Empty List'
        return self.top.data

if __name__ == '__main__':
    stackOne = Stack()
    stackOne.Push(10)
    stackOne.Push(20)
    stackOne.Push(30)

    while not stackOne.isEmpty():
        print(f'Popped: {stackOne.Pop()}')
