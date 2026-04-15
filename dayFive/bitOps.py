def bitState(num, pos):
    print(f'bitState({num}, {pos}) called from {__name__}')

def bitToggle(num, pos):
    print(f'bitToggle({num}, {pos}) called from {__name__}')

def toggleNibble(num, pos):
    print(f'toggleNibble({num}, {pos}) called from {__name__}')

def leftRotate(num, pos, nbits):
    print(f'leftRotate({num}, {pos}, {nbits}) called from {__name__}')

def rightRotate(num, pos, nbits):
    print(f'rightRotate({num}, {pos}, {nbits}) called from {__name__}')

if __name__ == '__main__':
    from sys import argv
    if len(argv) >= 3:
        first,second,third = int(argv[1]),int(argv[2]),int(argv[3])
    else:
        first, second, third = 10, 2, 3

    bitState(first, second)
    toggleNibble(first, second)
    leftRotate(first, second, third)