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
        newNode = Node(data)
        if self.head is None:
            self.head = newNode 
        else:
            temp = self.head 
            while temp.next:
                temp = temp.next
            temp.next = newNode 

    def insertPos(self, pos, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode 
        else:
            temp, cnt  = self.head, 1 
            while temp.next and cnt < pos - 1:
                temp = temp.next
                cnt += 1
            newNode.next = temp.next    
            temp.next = newNode 

    def deleteData(self, data):
        prev, temp = None, self.head
        while temp and temp.data != data:
            prev, temp = temp, temp.next
        
        if not temp:
            print(f'Data: {data} not found')
        elif temp == self.head:
            self.head = temp.next 
        else:
            prev.next = temp.next 

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
    
    for i in range(5):
        lstOne.insertEnd(201 + i)    
    lstOne.disp()
    
    lstOne.insertPos(3, 200)
    lstOne.disp()

    lstOne.deleteData(100)
    lstOne.disp()



