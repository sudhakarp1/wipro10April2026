from sys import argv

if __name__ =='__main__':
    print(f'argv: {argv}')
    print(f'script Name: {argv[0]}')
    print(f'Args: {argv[1:]}')
    print(f'Total Number of Args: {len(argv[1:])}')