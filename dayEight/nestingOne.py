'''
    Having Outer()
        inside Inner()
    Inner()        
'''
def OuterFun():
    print('Entering OuterFun()')
    def InnerFun():
        print('Entering InnerFun()')
    InnerFun()
    print('Exiting OuterFun()')

if __name__ == '__main__':
    OuterFun()