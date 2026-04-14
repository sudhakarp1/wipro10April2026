def fun():
    print('fun()...')

def funOne():
    print('1. funOne()...')
    fun()
    print('2. funOne()...')

def funTwo():
    print('1. funTwo()...')
    funOne()
    print('2. funTwo()...')

funTwo()
