class DoubleMe:
    def __init__(self, limit = 0):
        self.limit = limit 

    def __iter__(self):
        self.i = 1
        return self 

    def __next__(self):
        if self.i > self.limit:
            raise StopIteration
        temp = self.i * 2
        self.i += 1
        return temp 

for n in DoubleMe(10):
    print(n, end=' ')
        