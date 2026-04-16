'''
    Another Class Example
'''
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def getBalance(self):
        return self.balance

if __name__ == '__main__':
    objOne = BankAccount(5000)
    print(f'1. Balance--> {objOne.getBalance()}')
    objOne.deposit(1000)
    print(f'2. Balance--> {objOne.getBalance()}')
    objOne.withdraw(500)
    print(f'3. Balance--> {objOne.getBalance()}')