for cnt in (x for x in range(1,11)):
    print(f'cnt: {cnt}')

lstOne = [x for x in range(1,101)]
#
genOne = (x for x in range(1,101))
from sys import getsizeof
print(f'lstOne: {lstOne} --> {getsizeof(lstOne)}')
print(f'genOne: {genOne} --> {getsizeof(genOne)}')
