square = lambda a:  a * a 
print(f'type(square): {type(square)} --> {square(10)}')

Add = lambda a, b: a + b
print(f'Add(10,20) --> {Add(10, 20)}')

# map() --> apply function to an iterable(collection) --> collection
nums = [10, 20, 30, 40, 50, 60 ,70]
print(f'Using map() --> {list(map(lambda a: a + 2, nums))}')

# reduce() from functools module--> gives single output by 
# applying a function on an iterable
from functools import reduce 
print(f'Using reduce() --> {reduce(lambda a, b: a + b, nums)}')

# filter() gives a list based on a condition output by applying a function on an iterable
print(f'Using filter() --> {list(filter(lambda a: a % 20 == 0, nums))}')