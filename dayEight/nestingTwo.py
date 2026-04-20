'''
    Having Outer()
        inside Inner()
    Inner()        
'''
def OuterFun():
    print('Entering OuterFun()')
    def InnerFun():
        print('Entering InnerFun()')
    print('Exiting OuterFun()')
    return InnerFun

if __name__ == '__main__':
    newFun = OuterFun()
    print('In main')
    newFun()
