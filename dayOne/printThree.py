'''
    using fstrings or format strings
        fstring --> Python 3.0+
'''
#comments to be added

id, name,sal = 1001,'Sudhakar Palanivelu', 15000.92
print(f'1. id: {id:10}, name: {name:25}  sal: {sal:10.2f}')
print(f'2. id: {id:<10}, name: {name:<25}  sal: {sal:<10.2f}')
print(f'3. id: {id:>10}, name: {name:>25}  sal: {sal:>10.2f}')
print(f'4. id: {id:^10}, name: {name:^25}  sal: {sal:^10.2f}')
