'''
    calling with nesting
'''
def fiboCaller(num):
    res = {0:0, 1:1} #memoization
    def fibo(num):
        if num not in res:
            res[num] = fibo(num-1) + fibo(num-2)            
        return res[num] 
    
    for i in range(num):
        print(f'{i+1} --> {fibo(i)}')
    

if __name__ == '__main__':
    fiboCaller(4000)