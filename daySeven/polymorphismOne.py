'''
    
'''

class Animal:
    def sound(self):
        pass 

class Dog(Animal):
    def sound(self):
        print('bark...')

class Cat(Animal):
    def sound(self):
        print('meow meow...')

if __name__ == '__main__':
    cat = Cat()
    cat.sound()

    dog = Dog()
    dog.sound()
