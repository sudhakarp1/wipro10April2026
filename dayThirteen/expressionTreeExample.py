class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
    
    def __str__(self):
        return f'{self.data}'

class ExpressionTree:
    def __init__(self):
        self.root = None

    #Build from Postfix
    def buildFromPostfix(self, expression):
        stack = []

        for token in expression:
            if token.isdigit():  # operand
                stack.append(Node(token))
            else:  # operator
                right = stack.pop()
                left = stack.pop()

                node = Node(token)
                node.left = left
                node.right = right

                stack.append(node)

        self.root = stack[-1]
    
    def inOrder(self, node):
        if node:
            if node.left:
                print("(", end='')
            self.inOrder(node.left)
            print(node, end='')
            self.inOrder(node.right)
            if node.right:
                print(")", end='')
    
    def preOrder(self, node):
        if node:
            print(node, end=' ')
            self.preOrder(node.left)
            self.preOrder(node.right)    
    
    def postOrder(self, node):
        if node:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node, end=' ')

    def evaluate(self, node):
        if node is None:
            return 0

        # Leaf node
        if node.left is None and node.right is None:
            return int(node.data)

        left_val = self.evaluate(node.left)
        right_val = self.evaluate(node.right)

        if node.data == '+':
            return left_val + right_val
        elif node.data == '-':
            return left_val - right_val
        elif node.data == '*':
            return left_val * right_val
        elif node.data == '/':
            return left_val / right_val

if __name__ == '__main__':
    exp = ExpressionTree()

    # Postfix expression: (3 + 5) * (2 + 8) --> "35+28+*"
    exp.buildFromPostfix("35+28+*")

    print("inOrder (Infix): ", end="")
    exp.inOrder(exp.root)

    print("\npreOrder (Prefix): ", end="")
    exp.preOrder(exp.root)

    print("\npostOrder (Postfix): ", end="")
    exp.postOrder(exp.root)

    print("\nEvaluated Result:", exp.evaluate(exp.root))
