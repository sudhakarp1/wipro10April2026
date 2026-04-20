def funOne(): #generator 
    var = 100
    print('statement #1')
    yield var # generators yield where functions return
    var = 200
    print('statement #2')
    yield var
    var = 300
    print('statement #3')
    yield var

obj = funOne() #returns a generator object
'''
for i in obj:
    print(f'i: {i}')
'''
print(next(obj)) #return individual value from object obj
print(next(obj)) 
print(next(obj)) 
#print(next(obj)) 