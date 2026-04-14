def funOne(x, y, z=100, *args):
    print(f'x: {x}  y: {y}  z: {z}  args: {args}')

funOne(10,20)
funOne(10,20,30,31,32,33,34)