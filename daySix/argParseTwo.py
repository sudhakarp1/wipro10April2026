import argparse
parser = argparse.ArgumentParser(description="Expr command Implementation")
#positional arguments: operand1, operator, operand2
parser.add_argument('-a', '--add', nargs=2, type=float, help="Add option passed")

args = parser.parse_args()
if args.add:
    print(f'Add Option selected: {args.add[0]} + {args.add[1]}')
