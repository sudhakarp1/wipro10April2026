'''
Encapsulation:
    Bringing data + functions together is encapsulation in 
    addition to restricting access
        In languages like C++/Java/C# --> protected and private 
        In Python -- all members are public by default
                  -->No special keywords like protected and private
        we follow naming convention
            _name ==> protected
            __name --> private     
'''
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def getBalance(self):
        return self.__balance

if __name__ == '__main__':
    objOne = BankAccount(5000)
    print(f'1. Balance--> {objOne.getBalance()}')
    objOne.deposit(1000)
    print(f'2. Balance--> {objOne.getBalance()}')
    objOne.withdraw(500)
    print(f'3. Balance--> {objOne.getBalance()}')