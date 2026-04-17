class NumOps:
    @staticmethod
    def bitState(num, pos):
        print(f'num: {num} and pos {pos}')

    #other bit functions can be added here 
    @staticmethod
    def isEven(num):
        return num % 2 == 0
    
if __name__ == '__main__':
    NumOps.bitState(10,2)
    print(f'Num: 101 --> {NumOps.isEven(101)}')
