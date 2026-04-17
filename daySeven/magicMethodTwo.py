'''
    dunder(magic/special) methods 
    __methodName__ ==> 
'''

class Number:
    def __init__(self, num):
        self._num = num

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self._num + other._num)
        elif isinstance(other, int):
            return Number(self._num + other)
        else:
            return NotImplemented
        
    def __str__(self):
        return f'Num: {self._num}'
    
if __name__ == '__main__':
    numOne = Number(100)
    print(f'{numOne}')
    numTwo = Number(200)
    print(f'{numTwo}')

    numThree = numOne + numTwo
    print(f'{numThree}')

    numFour = numOne + 1000
    print(f'{numFour}')