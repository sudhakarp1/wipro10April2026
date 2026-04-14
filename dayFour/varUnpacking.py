x, y, z = 11, 22, 33
print(f'x: {x}  y:{y}  z: {z}')

x, y, *z = 11, 22, 33, 44, 55, 66
print(f'x: {x}  y:{y}  z: {z}')

x, *y, z = 11, 22, 33, 44, 55, 66
print(f'x: {x}  y:{y}  z: {z}')

*x, y, z = 11, 22, 33, 44, 55, 66
print(f'x: {x}  y:{y}  z: {z}')

*x, y, z = 11, 22
print(f'x: {x}  y:{y}  z: {z}')
