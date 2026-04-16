def evalExpr():
    validOps = ['+','-','*','/','//', '%','**']
    res = 0
    if len(argv[1:]) != 3:
        print(f'Invalid number of args {argv[1:]}')        
        return 
    operand1, operator, operand2 = argv[1:]
    operand1, operand2 = int(operand1), int(operand2)
    if operator in validOps:
        if operator=='+': 
            res = operand1 + operand2 
        elif operator=='-': 
            res = operand1 * operand2 
        elif operator=='*': 
            res = operand1 * operand2 
        elif operator=='/': 
            res = operand1 * operand2 
        elif operator=='%': 
            res = operand1 * operand2 
        elif operator=='//': 
            res = operand1 // operand2 
        elif operator=='**': 
            res = operand1 ** operand2 
    else:
        print(f'Invalid operation: {operator}')

    return res 

if __name__ == '__main__':
    from sys import argv 
    print(evalExpr())


