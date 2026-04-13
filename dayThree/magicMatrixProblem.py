'''
Create an odd square matrix and fill the elements in such a way were sum o each row, rowumn and diagonal elements are same. (Also referred to as magic matrix)
Algorithm:
	1. start with mid column on top row. 
	2. If curr pos is on top row -> go to bottom row + 1 column 
	3. If on right most column -> got to first column -1 row 
	4. if right diagonal position is free --> fill It 
	5. None of the above conditions got down one row 
'''

row = int(input('Enter row size:'))
mat = []
for _ in range(row):
    mat.append([0] * row)

if row % 2 == 1: #magic filling 
    rCnt, cCnt,num = 0, row//2, 1
    #last = num + row * row - 1
    while num <= row * row:
        #print(f'{rCnt},{cCnt} --> {num}', end= '--> ')
        mat[rCnt][cCnt] = num
        if rCnt == 0 and cCnt != row - 1:            
            rCnt,cCnt = row - 1, cCnt + 1
        elif cCnt == row - 1 and rCnt != 0:            
            rCnt, cCnt = rCnt - 1, 0
        elif cCnt != row -1 and rCnt !=0 and mat[rCnt - 1][cCnt + 1] == 0:            
            rCnt, cCnt = rCnt - 1, cCnt + 1
        else:            
            rCnt += 1
        num+=1        
else:
    #normal filling
    pass


        
print('Matrix: ')
for eachRow in mat:
    for element in eachRow:
        print(f'{element: 4}', end='')
    print()
