from copy import deepcopy
lstOne = [11,22,33]
lstOne.append([55,66,77])

#lstTwo = lstOne.copy() #still shalow copy
lstTwo = deepcopy(lstOne) #deep copying

print(f'1. lstOne: {lstOne}--> {id(lstOne)}')
print(f'1. lstTwo: {lstTwo}--> {id(lstTwo)}')
lstOne[3].append(1000)
print(f'2. lstOne: {lstOne}--> {id(lstOne)}')
print(f'2. lstTwo: {lstTwo}--> {id(lstTwo)}')
