'''
Formatted output using C Language Style:
    C style format specifiers (commonly used)
        %c --> Character
        %d --> signed integer
        %u --> unsigned integer
        %f --> float (Fixed notation)
        %e --> float (exponential/scientific notation)
        %s --> string
        ---> %spacing Width character
        for example:
            ---> %10s
            ---> %10d --> right aligned (by default)
                 %-10d --> left aligned
            ---> %10u
'''

var = 100
print('C style: var: %-10d, var: %o  var: %X' % ( var, var, var))
