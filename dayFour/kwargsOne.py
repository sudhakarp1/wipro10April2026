def funOne(**kwargs):
    print(f'kwargs: {kwargs}')

def funTwo(x, y, z=100, *args, **kwargs):
    print(f'x: {x}  y: {y}  z: {z}  args: {args} kwargs: {kwargs}')

funTwo(10, 20)
funTwo(10, 20, 30, 31, 32, 33, 34)
funTwo(10, 20, 30, 31, 32, 33, 34, name='Some name here')
#funOne(a=10, b=20, name='Suryudu')
