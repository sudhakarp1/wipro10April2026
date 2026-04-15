try:
    num = int(input('Enter a num: ')) #ValueError
    exp = 100 / 0     #ZeroDivisionError
except ValueError as veObj:
    print(f'ValueError: --> Handled here --> {veObj}')
except ZeroDivisionError as ze:
    print(f'ZeroDivisionError --> {ze}')
else:
    print(f'Num Entered is : {num}')

print('program continues...') 