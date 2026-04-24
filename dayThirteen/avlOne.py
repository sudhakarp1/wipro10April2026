class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None 
        self.height = 1 #height
    
    def __str__(self):
        return f'{self.data}'

class AVLTree:
    def __init__(self):
        self.root = None 
    
    def _height(self, node):
        return node.height if node else 0
    
    def _balance(self, node):
        return self._height(node.left) - self._height(node.right) 
    
    def _rightRotate(self, curr):
        temp = curr.left
        ST1 = temp.right

        temp.right = curr 
        curr.left = ST1 

        curr.height = 1 + max(self._height(curr.left),self._height(curr.right) )
        temp.height = 1 + max(self._height(temp.left),self._height(temp.right) )

        return temp

    def _leftRotate(self, curr):
        temp = curr.right
        ST1 = temp.left

        temp.left = curr 
        curr.right = ST1 

        curr.height = 1 + max(self._height(curr.left),self._height(curr.right) )
        temp.height = 1 + max(self._height(temp.left),self._height(temp.right) )

        return temp
    
    def insert(self, data):
        self.root = self._InnerHelper(self.root, data)#recursive

    def _InnerHelper(self, root, data):
        if not root:
            return Node(data)
        
        if data < root.data:
            root.left = self._InnerHelper(root.left, data)
        else:
            root.right = self._InnerHelper(root.right, data)   

        root.height =  1 + max(self._height(root.left),self._height(root.right))
        balanceFactor = self._balance(root)
            
        #rotations based on balanceFactor 
        if balanceFactor > 1 and data < root.left.data:
            return self._rightRotate(root)
        
        if balanceFactor < -1 and data > root.right.data:
            return self._leftRotate(root)
        
        if balanceFactor > 1 and data > root.right.data:
            root.left = self._leftRotate(root.left)
            return self._rightRotate(root)
        
        if balanceFactor < -1 and data < root.right.data:
            root.right = self._rightRotate(root.right)
            return self._leftRotate(root)
        
        return root 

    def preOrder(self, root):
        if root:
            print(root, end=' ')
            self.preOrder(root.left)
            self.preOrder(root.right)

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root, end=' ')
            self.inOrder(root.right)

    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root, end=' ')            

if __name__ == '__main__':
    avl = AVLTree()
    lst = [5, 10, 20, 33, 35,36, 50, 66, 68, 70, 75, 78, 88, 90, 100]
    for data in lst:
        avl.insert(data)
    '''
    print('In Order: ', end=' ')
    avl.inOrder(avl.root)
    
    print('Post Order: ', end=' ')
    avl.postOrder(avl.root)
    '''
    print('Pre Order: ', end=' ')
    avl.preOrder(avl.root)

