def doubleMe(limit=0):
    n = 1 
    while n < limit:
        yield n * 2
        n += 1

for n in doubleMe(10):
    print(n, end=' ')
