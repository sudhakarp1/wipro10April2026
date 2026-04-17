'''
    dunder(magic/special) methods 
    __methodName__ ==> 
'''

class Number:
    def __init__(self, num):
        self._num = num

    def __add__(self, other):
        return Number(self._num + other._num)
        
    def __str__(self):
        return f'Num: {self._num}'
    
if __name__ == '__main__':
    numOne = Number(100)
    print(f'{numOne}')
    numTwo = Number(200)
    print(f'{numTwo}')

    numThree = numOne + numTwo
    print(f'{numThree}')

