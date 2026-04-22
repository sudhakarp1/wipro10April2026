class Node:
    def __init__(self, data):
        self.data, self.next, self.prev = data, None, None
    
    def __str__(self):
        return f'data: {self.data} Prev: {self.prev} Next: {self.next}'

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def insertBegining(self, data):
        newNode = Node(data) 

        if self.head:
            self.head.prev = newNode
            newNode.next = self.head 
        else:
            self.tail = newNode
        
        self.head = newNode
		
    def insertEnd(self, data):
        newNode = Node(data) 
        if self.head is None: 
            self.head = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail

        self.tail = newNode

    def insertPos(self, pos, data):
        newNode = Node(data) 
        print(f'pos: {pos} data: {data}')
        if self.head is None: #empty list
            self.head = self.tail = newNode
            return

        if pos == 0:
            self.head.prev = newNode
            newNode.next = self.head             
            self.head = newNode
        else:
            temp, cnt = self.head, 1        
            while temp and cnt < pos:#getting position
                cnt, temp = cnt + 1, temp.next

            if temp is None:
                print(f' Position {pos} out of index')
            else:
                newNode.next = temp.next 
                newNode.prev = temp

                if temp.next:
                    temp.next.prev = newNode
                    temp.next = newNode
                else:
                    temp.next = newNode
                    self.tail = newNode
            

    def deleteData(self, data):
        prev, temp = None, self.head 
        while temp and temp.data != data: #temp will stop at correct node
            prev, temp = temp, temp.next 
        
        if temp is None:
            print(f'Data: {data} not found')
        elif prev is None:
            self.head = temp.next 
            if self.head:
                self.head.prev = None
        else:
            if temp.next: #middle positions
                temp.next.prev = prev 
                prev.next = temp.next
            else:#last position                
                prev.next = None
                self.tail = prev
                

    def dispForward(self):
        print(f'Forward Print: ',end='')
        temp = self.head
        while temp:
            print(f'{temp.data}', end='-->')
            temp = temp.next
        print('None')       

    def dispReverse(self):
        print(f'Reverse Print: ',end='')
        temp = self.tail
        while temp:
            print(f'{temp.data}', end='-->')
            temp = temp.prev
        print('None')

if __name__ == '__main__':
    lstOne = LinkedList()
    for i in range(3):
        lstOne.insertBegining(100 + i)
    
    lstOne.dispForward()
    lstOne.dispReverse()
    print('* ' * 40 )


