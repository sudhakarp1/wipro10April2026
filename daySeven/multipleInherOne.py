class BaseOne:
    pass 

class BaseTwo:
    pass 

class Derived(BaseOne, BaseTwo):
    pass 

if __name__ =='__main__':
    obj = Derived()
