'''
    Inheritance:
        creating a new class by extending the existing class

        Parent/Base/Super class --> Existing class
        Child/Derived/Sub class --> New class being created 

        The Idea of Inheritance from OOP point of view is to 
        extend the base class without modifying the existing class.

        Open/Close principle:
            Open for extension by closed for modification
'''

class Base:
    def __init__(self, data = 10):
        self.dataOne, self.dataTwo = data, data + 100

    def methodOne(self):
        print(f'in methodOne() --> dataOne: {self.dataOne}') 

    def methodTwo(self):
        print(f'in methodTwo() --> dataTwo: {self.dataTwo}') 

class Derived(Base):
    def __init__(self, data=10):
        super().__init__(data)
        self.dataThree = data + 200

    def methodThree(self):
        print(f'dataOne: {self.dataOne}  dataTwo: {self.dataTwo}  datThree: {self.dataThree}')

if __name__ == '__main__':
    obj = Derived(100)
    obj.methodOne()
    obj.methodTwo()
    obj.methodThree()
