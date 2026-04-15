'''
#method #1
import myPkgOne.bitOps

if __name__ =='__main__':
    myPkgOne.bitOps.bitState(10,20)

#method #2
import myPkgOne.bitOps as mypk

if __name__ =='__main__':
    mypk.bitState(10,20)
'''
#method #2
from myPkgOne import bitOps as bo
from myPkgOne import numOps as no

if __name__ =='__main__':
    bo.bitState(10,20)
    no.isPrime(100)