'''
    used in binary search --> Eliminative search --> middle search
'''

n, cnt = 1000000,  1
while n > 0:
    print(f'cnt: {cnt} n : {n}')
    n, cnt =   n // 2 , cnt + 1
