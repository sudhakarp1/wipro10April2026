try:
    num = int(input('Enter a num: '))
except ValueError as veObj:
    print(f'ValueError: --> Handled here --> {veObj}')
else:
    print(f'Num Entered is : {num}')

print('program continues...') 