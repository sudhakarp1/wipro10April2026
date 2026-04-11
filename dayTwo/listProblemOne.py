lst = []
start = int(input('Enter first Number: '))
for i in range(100):
    lst.append(start+i)

print(f'list: {lst}')

for i in range(100):
    for div in range(2, lst[i]):
        if lst[i] % div == 0:
            lst[i] = 0
            break

print(f'list: {lst}')    

zCount, maxZCount, first, last = 0,0,0,0
for idx in range(len(lst)):
    if lst[idx] == 0:
        zCount+=1
    else:
        if zCount > maxZCount:
            maxZCount = zCount
            last, first = lst[idx], lst[idx - maxZCount -1]
        zCount = 0

print(f'{maxZCount} zeroes between {first} and {last}')
