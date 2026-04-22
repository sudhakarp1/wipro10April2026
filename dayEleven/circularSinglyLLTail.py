class Node:
    def __init__(self, value):
        self.data, self.next = value, None 

    def __str__(self):
        return f'{self.data}'
    
class CircularSingleLL:
    def __init__(self):
        self.head, self.tail = None, None

    def insertBegining(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = self.tail = newNode
            newNode.next = newNode            
            return 
        
        newNode.next = self.head #existing head as second 
        self.tail.next = newNode #last node storing first node address
        self.head = newNode #newNode as head node 

    def insertEnd(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = self.tail = newNode
            newNode.next = newNode            
            return 
        
        newNode.next = self.head #existing head as second 
        self.tail.next = newNode #last node storing first node address
        self.tail = newNode #newNode as head node 

    def insertPos(self, pos, value):
        pass
    
    def deletePos(self, pos):
        pass

    def deleteValue(self, value):
        pass

    def disp(self):
        if self.head is None:
            print('Empty List')
            return
        
        temp = self.head
        while True:
            print(temp, end='-->')
            temp = temp.next
            if temp == self.head:
                break 

        print('head')

if __name__ == '__main__':
    lstOne = CircularSingleLL()
    for i in range(5):
        lstOne.insertEnd(100 + i)
    
    lstOne.disp()