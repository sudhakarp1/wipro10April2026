'''
    expr command using argparse module
'''
import argparse
def evalExpr():
    parser = argparse.ArgumentParser(description="Expr command Implementation")
    #positional arguments: operand1, operator, operand2
    parser.add_argument('operand1', type=int, help="First number")
    parser.add_argument('operator',choices = ['+','-','*','/','%','//','**'], help='Operator(+,-,*,/)')
    parser.add_argument('operand2', type=int, help="Second number")

    args = parser.parse_args()
    res = 0
    if args.operator == '+':
        res = args.operand1 + args.operand2
    elif args.operator == '-':
        res = args.operand1 - args.operand2
    elif args.operator == '*':
        res = args.operand1 * args.operand2
    elif args.operator == '/':
        res = args.operand1 / args.operand2
    elif args.operator == '%':
        res = args.operand1 % args.operand2
    elif args.operator == '//':
        res = args.operand1 // args.operand2
    elif args.operator == '**':
        res = args.operand1 ** args.operand2
    else:
        print('Invalid Operator')

    return res

if __name__ == '__main__':
    print(evalExpr())