lstOne = [11,22,33]
#lstTwo = lstOne #referencing
lstTwo = lstOne.copy() #still shalow copy

print(f'1. lstOne: {lstOne}--> {id(lstOne)}')
print(f'1. lstTwo: {lstTwo}--> {id(lstTwo)}')
lstOne.append(44)
print(f'2. lstOne: {lstOne}--> {id(lstOne)}')
print(f'2. lstTwo: {lstTwo}--> {id(lstTwo)}')
lstOne.append([55,66,77])
print(f'3. lstOne: {lstOne}--> {id(lstOne)}')
print(f'3. lstTwo: {lstTwo}--> {id(lstTwo)}')
lstOne[4].append(1000)
print(f'4. lstOne: {lstOne}--> {id(lstOne)}')
print(f'4. lstTwo: {lstTwo}--> {id(lstTwo)}')