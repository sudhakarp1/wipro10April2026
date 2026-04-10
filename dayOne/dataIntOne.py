var = 100
print('C style: var: %d, var: %o  var: %X' % ( var, var, var))
print('Python Old: var:{} , var: {}  var: {} var: {}'.format( var, oct(var), hex(var), bin(var)))
print(f'Python 3.0 Onwards var: {var} var: {var:o} var: {var:x} var: {var:b}')
