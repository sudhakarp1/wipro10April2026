class Employee:
    companyName = 'Wipro' #class member
    def __init__(self, name):
        self.name = name #instance / object member

    def disp(self): #instance member
        print(f'name: {self.name} --> company: {self.companyName}')

if __name__ =='__main__':
    empObject = Employee('Upendra')
    empObject.disp()

    empObject = Employee('Chandu')
    empObject.disp()