mat,num = [], 1
row = int(input('Enter row size: '))
col = int(input('Enter col size: '))
for i in range(row):
    mat.append([]) #empty nested lists --> rows
    for j in range(col):
        mat[i].append(num) #inserting elements in each row
        num+=1

#print(mat)

for eachRow in mat:
    for val in eachRow:
        print(f'{val}', end=' ')
    print()
