'''
    Custom/user defined iterator
'''

class IterClass:
    def __init__(self, start, end):
        self.current, self.end = start, end 
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current+=1
        return value 
  
for cnt in IterClass(10,20):
    print(f'{cnt}',end=' ')
