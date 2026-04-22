class Node:
    def __init__(self, value):
        self.data, self.next = value, None 

    def __str__(self):
        return f'{self.data}'
    
class CircularSingleLL:
    def __init__(self):
        self.head = None

    def insertBegining(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            newNode.next = newNode
            return 

        temp = self.head 
        while temp.next != self.head: #finding out last node
            temp = temp.next 

        newNode.next = self.head #existing head as second 
        temp.next = newNode #last node storing first node address
        self.head = newNode #newNode as head node 

    def insertEnd(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            newNode.next = newNode
            return 

        temp = self.head 
        while temp.next != self.head: #finding out last node
            temp = temp.next 

        newNode.next = self.head #existing head as second 
        temp.next = newNode #last node storing first node address
    
    def insertPos(self, pos, value):
        if pos == 0:
            self.insertBegining(value)
            return 
        
        temp, cnt = self.head, 1
        while cnt < pos and temp != self.head:
            cnt, temp = cnt + 1, temp.next
        
        if temp == self.head:
            raise IndexError(f'{pos}: out of range')

            #print('pos {pos} Out of range')
            #return
        
        newNode = Node(value)
        newNode.next = temp.next
        temp.next = newNode        
    
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
    lstOne.insertPos(0, 1000)
    lstOne.insertPos(15, 2000)
    lstOne.disp()