gvar = 100

def OuterFun():
    global gvar #introducing global variable in this scope
    print(f'1. OuterFun() gvar: {gvar}')
    def InnerFun():
        global gvar #introducing global variable in this scope
        print(f'1. InnerFun() gvar: {gvar}')
        gvar+=10
    gvar += 10
    InnerFun()

if __name__ == '__main__':
    OuterFun()
