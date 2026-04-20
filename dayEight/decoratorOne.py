def HigherFun(func):
    def LowerFun(*args):
        print(f'Before calling ... {args}')
        res = func(*args)
        print(f'After calling ... {args}')
        return res
    return LowerFun #return function address

def AddThree(x, y, z):
    return x + y + z

def AddTwo(x, y):
    return x + y

if __name__ == '__main__':
    funOne = HigherFun(AddThree)
    res = funOne(10,20,30)
    print(f'Res: {res}')
    
    funOne = HigherFun(AddTwo)
    res = funOne(10,20)
    print(f'Res: {res}')
        