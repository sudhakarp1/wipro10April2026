'''
Formatted output using C Language Style:
    C style format specifiers (commonly used)
'''

id, name,sal = 1001,'Sudhakar Palanivelu', 15000.92
print('1. id: %10d, name: %25s  sal: %10.2f' % (id, name, sal))
print('2. id: %-10d, name: %-25s  sal: %-10.2f' % (id, name, sal))
