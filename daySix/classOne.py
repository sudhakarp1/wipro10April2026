'''
    A simple class Demo
'''

class Person:
    def __init__(self, name, age):#constructor
        self.name, self.age = name, age 

    def disp(self):
        print(f'name: {self.name}   age: {self.age}')


if __name__ == '__main__':
    obj = Person('Sachin Tendulkar', 51)
    obj.disp()