class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None 
    
    def __str__(self):
        return f'{self.data}'

class BSTree:
    def __init__(self):
        self.root = None

    def Insert(self, data): #Iterative method
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return 
        
        prev, curr = None, self.root
        while curr:
            prev = curr
            if data < curr.data:
                curr = curr.left 
            else:
                curr = curr.right
        
        if data < prev.data:
            prev.left = newNode
        else:
            prev.right = newNode        

    def remove(self, data):        
        pCurr,  curr = None, self.root
        while curr and curr.data != data:
            pCurr = curr 
            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None:
            print(f'{data} Not Found')
        elif curr.left is None: #leaf or Parent with 1 child 
            temp = curr.right
        elif curr.right is None: #leaf or Parent with 1 child 
            temp = curr.left
        else: #Parent with 2 children
            pSucc, succ = None, curr.right
            while succ.left:
                pSucc = succ 
                succ = succ.left
            
            if pSucc is None:
                succ.left = curr.left 
            else:
                pSucc.left = succ.right
                succ.left = curr.left 
                succ.right = curr.right 

            temp = succ 
        
        if pCurr is None:
            self.root = temp 
        elif pCurr.left == curr:
            pCurr.left = temp 
        else:
            pCurr.right = temp 

    def dispBST(self):
        print('Printing BST') 
        '''
        print(f'Pre-Order: ', end='')
        self.preOrder(self.root)
        '''
        print(f'In-Order: ', end='')
        self.inOrder(self.root)
        '''
        print(f'\nPost-Order: ', end='')
        self.postOrder(self.root)
        '''
        print('\n' + '* ' * 40)

    def preOrder(self, root): #R'LR  
        if root:
            print(root, end='  ') #processing root node
            self.preOrder(root.left)
            self.preOrder(root.right)
        
    def inOrder(self, root): #LR'R  
        if root:
            self.inOrder(root.left)
            print(root, end='  ') #processing root node
            self.inOrder(root.right) 
    
    def postOrder(self, root):#LRR'  
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right) 
            print(root, end='  ') #processing root node        
        

if __name__ == '__main__':
    data = [50, 30, 80, 10, 20, 60, 100, 54, 58, 52, 70, 65, 78, 5, 15, 25]
    bst = BSTree()
    for value in data:
        bst.Insert(value)

    bst.dispBST()
    bst.remove(78)
    bst.remove(30)
    bst.remove(50)
    bst.dispBST()


