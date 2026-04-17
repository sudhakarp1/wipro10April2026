class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value 
        self.mesg = f'Negative value {value} is not allowed'
        super().__init__(self.mesg)
    
def factorial(num):
    if num < 0:
        raise NegativeValueError(num)
    elif num <= 1:
        return 1
    return num * factorial(num - 1)

if __name__ == '__main__':
    try:
        print(f'factorial(5) --> {factorial(5)}')
        print(f'factorial(-4) --> {factorial(-4)}')
    except NegativeValueError as ne:
        print(f'Exception occurred: {ne}')
