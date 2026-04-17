'''
    sample debug
'''

import pdb
pdb.set_trace() # inserting break point

def myFun(cnt):
    print(f'cnt: {cnt}')

cnt = 1
while cnt <= 10:
    myFun(cnt)    
    cnt+=1
