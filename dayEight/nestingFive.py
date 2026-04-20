def operationFun(func):
    print(f'1.Before operationFun()...')
    func()
    print(f'1.After operationFun()...')
    print('*' * 50)

def funOne():
    print('funOne()...called')

def funTwo():
    print('funTwo()...called')

if __name__ == '__main__':
    operationFun(funOne) #function funOne is passed as argument
    operationFun(funTwo) #function funTwo is passed as argument
