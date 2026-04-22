'''
    stacks implementation :
        with List as underlying data structure
'''

class Stack:
    def __init__(self):
        self.stk = []
    
    def push(self, data):
        self.stk.append(data)

    def pop(self):
        if self.isEmpty():
            return f'Stack Underflow'
        return self.stk.pop()
    
    def isEmpty(self):
        return len(self.stk) == 0
    
    def peek(self):
        if self.isEmpty():
            return f'Empty Stack'        
        return self.stk[-1]
    
    def disp(self):
        print(self.stk)

if __name__ == '__main__':
    stackOne = Stack()
    stackOne.push(10)
    stackOne.push(20)
    stackOne.push(30)
    stackOne.disp()

    print(stackOne.peek())
    print(stackOne.pop())
    stackOne.disp()