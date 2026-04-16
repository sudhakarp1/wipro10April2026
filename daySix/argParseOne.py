import argparse

parser = argparse.ArgumentParser(description='An Example')
parser.add_argument('name', help='Names ...')
parser.add_argument('mesg', help='message ')

args = parser.parse_args()
print(f'Hello {args.name}...{args.mesg}')
