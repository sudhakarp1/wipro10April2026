class Employee:
    company = 'Wipro'

    def __init__(self,id, name, sal):
        self.id, self.name, self.sal = id, name, sal 
    
    @classmethod
    def fromString(cls, data):
        id,name,sal = data.split(',')
        return cls(id, name, sal)

    def disp(self):
        print(f'Id: {self.id}  Name: {self.name}  Sal: {self.sal}')

if __name__ == '__main__':
    chandu = Employee(1001, 'Charan Chandu', 300000)
    chandu.disp()

    nikesh = Employee.fromString('1002,Nikesh Naidu,400000')
    nikesh.disp()
