'''
    calling with nesting
'''
from functools import lru_cache

def fiboCaller(num):
    @lru_cache()
    def fibo(num):
        if num <= 1:
            return num
        return fibo(num-1) + fibo(num-2) 
    
    for i in range(num):
        print(f'{i+1} --> {fibo(i)}')
    
if __name__ == '__main__':
    fiboCaller(4000)