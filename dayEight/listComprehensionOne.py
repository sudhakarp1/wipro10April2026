#using a loop
lstOne = [x for x in range(1,11)]
print(lstOne)

#loop with condition --> simple if 
lstTwo = [x for x in range(20) if x % 2]
print(lstTwo)
#loop with condition --> if else
lstThree = [x if x % 2 == 0 else 0 for x in range(20)]
print(lstThree)

#nesting of loops 
lstFour = [(x,y) for x in range(1,6) for y in 'abcde']
print(lstFour)

#2D matrix to 1D list
mat = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
matFlat = [num for row in mat for num in row]
print(matFlat)

strings = '1,2,3,4,5,6,7,8,9,10'
listFive = [int(x) for x in strings.split(',')]
print(listFive)