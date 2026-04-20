class Node:
    def __init__(self, data):
        self.data, self.next = data, None
    
    def __str__(self):
        return f'data: {self.data} Next: {self.next}'

class LinkedList:
    def __init__(self):
        self.head = None 

    def insertBegining(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode 
        else:
            newNode.next = self.head 
            self.head = newNode

    def insertEnd(self, data):
        pass 

    def insertPos(self, pos, data):
        pass

    def deleteData(self, data):
        pass 

    def disp(self):
        tempNode = self.head 
        print('Linked List: ',end='')
        while tempNode:
            print(tempNode.data, end='-->')
            tempNode = tempNode.next
        print('None')

if __name__ == '__main__':
    lstOne = LinkedList()
    for i in range(5):
        lstOne.insertBegining(100 + i)    
    lstOne.disp()


