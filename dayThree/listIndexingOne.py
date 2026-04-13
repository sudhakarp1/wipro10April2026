'''
    Indexing --> accessing elements using index --> []
        index starts with 0
        slice --> part of the list by specifying the range
        [start: end: incr] # the end element is not considered
'''
lstOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(lstOne[:5]) # 0 - 4 
print(lstOne[5:]) # lstOne[5] onwards + all elements )
print(lstOne[:]) #all elements
print(lstOne[0:len(lstOne):1])#0 to last incr by 1
print(lstOne[0:len(lstOne):2])#0 to last incr by 2
print(lstOne[0:len(lstOne):3])#0 to last incr by 2

print(lstOne[len(lstOne):0:-1])#last to second element
print(lstOne[::-1])#Reversing the list
