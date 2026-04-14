'''
#inside usingModOne.py
#method #1
import modOne

if __name__ == '__main__':
    modOne.funOne()
    print(modOne.lstOne)
    print(modOne.lstTwo)
    modOne.funTwo()

#method #2
import modOne as mo

if __name__ == '__main__':
    mo.funOne()
    print(mo.lstOne)
    print(mo.lstTwo)
    mo.funTwo()
'''
#method #3
if __name__ =='__main__':
    from modOne import lstOne, funOne, funTwo
    print(lstOne)
    funOne()
    funTwo()

