'''
    Efficiency of your algorithm 
        amount of time taken to execute a function.
'''
from time import perf_counter

def calculateTime(func):    
    def funCaller(*arg):
        start = perf_counter()        
        func(*arg)
        end = perf_counter()
        print(f'{func.__name__} --> {round(end - start, 3)}')
    return funCaller    

@calculateTime
def funDemo(num):#linear Algorithm
    for _ in range(num):
        pass

if __name__ == '__main__':
    funDemo(1000)
