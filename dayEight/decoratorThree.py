def HigherFun(func):
    def LowerFun(*args):
        print(f'Before calling ... {args}')
        res = func(*args)
        print(f'After calling ... {args}')
        return res
    return LowerFun #return function address

@HigherFun #decorated
def AddThree(x, y, z):
    return x + y + z

@HigherFun
def AddTwo(x, y):
    return x + y

if __name__ == '__main__':
    res = AddThree(10,20,30)
    print(f'Res: {res}')
    
    res = AddTwo(10,20)
    print(f'Res: {res}')
        