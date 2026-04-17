'''
    
'''
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass 

class Dog(Animal):    
    def sound(self):#enforcing the overriding
        print('bark...')
    
class Cat(Animal):
    def sound(self):#enforcing the overriding
        print('meow meow...')

if __name__ == '__main__':
    cat = Cat()
    cat.sound()

    dog = Dog()
    dog.sound()
