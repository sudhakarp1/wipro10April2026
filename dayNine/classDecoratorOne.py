class DecoratorExample:
    def __init__(self, func):
        self.func = func 

    def __call__(self, *args, **kwds):
        print('1. Before Calling...')
        res = self.func(*args, **kwds)
        print('2. After Calling...')
        print('*' * 50)
        return res 

@DecoratorExample
def AddTwo(a, b):
    return a + b 

@DecoratorExample
def AddThree(a, b, c):
    return a + b + c

@DecoratorExample
def AddMany(*args):
    return sum(args)

if __name__ == '__main__':
    print(f'10 + 20 ---> {AddTwo(10, 20)}')
    print(f'10 + 20 + 30 ---> {AddThree(10, 20, 30)}')
    print(f'10 .. 60 ---> {AddMany(10, 20, 30, 40, 50, 60)}')

