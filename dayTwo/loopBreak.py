'''
    usage of break in a loop
'''
num =101
for var in range(2, num):
    if num % var == 0:
        break
else:
    print(f'Num: {num} is a Prime number')

