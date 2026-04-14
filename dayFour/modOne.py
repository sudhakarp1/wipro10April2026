'''
    Intro to user defined modules
        data, functions, classes 
'''
#modOne.py
lstOne = [10, 11, 22, 33]
lstTwo = ['name #1','name #2','name #3','name #4','name #5']

def funOne():
    print(f'funOne()... {__name__}') #double underscore
                                      #dunder  name 
def funTwo():
    print(f'funTwo()... {__name__}')

def funThree():
    print(f'funThree()... {__name__}')

if __name__ == '__main__':
    funOne()
    funTwo()
    funThree()
