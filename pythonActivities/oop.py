"""
class House:
    numOfDoors = 0
    furniture = []
    isLocked = True
    
    
kevinHouse = House()
kevinHouse.numOfDoors = 7

print(kevinHouse.numOfDoors)

class Pet:
    def __init__(self, name, hasLegs, age):
        self.name = name
        self.hasLegs = hasLegs
        self.age = age

    def intro(self):
        print(self.name, "is", self.age, "years old.")

cat1 = Pet("Dog", True, 7)
dog1 = Pet("Sage", True, 5)

dog1.intro()
cat1.intro()
"""

"""
class ATM:
    def __init__(self):
        self.bankAccount = None
    
    def deposit(self):
        amount = float(input("Enter the amount you want to deposit: $"))
        if amount > 0:
            print("You have deposited $", amount," successfully.")
            self.bankAccount.balance = self.bankAccount.balance + amount
        else:
            print("Invalid deposit.")
        
    def withdraw(self):
        amount = float(input("Enter the amount you want to withdraw: $"))
        if amount > 0:
            if amount <= self.bankAccount.balance:
                print("You have withdrawn $", amount, " successfully.")
                self.bankAccount.balance = self.bankAccount.balance - amount
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal.")

    def checkBalance(self):
            print("Your current balance is $", self.bankAccount.balance)



class bankAccount:
    def __init__(self, name, pin, balance = 0):
        self.name = name
        self.pin = pin
        self.balance = balance


user1 = bankAccount("Kevin", 1234, 1000)
user1ATM = ATM()
user1ATM.bankAccount = user1

user1ATM.deposit()
user1ATM.checkBalance()
user1ATM.withdraw()
user1ATM.checkBalance()"""

class ATM:
    def __init__(self):
        self.bankAccount = None
        self.authenticated = False

    def insertCard(self, account):
        entered_pin = int(input("Enter your PIN: "))
        if entered_pin == account.pin:
            self.bankAccount = account
            self.authenticated = True
            print("PIN verified. Access granted.")
        else:
            print("Incorrect PIN. Access denied.")

    def deposit(self):
        if not self.authenticated:
            print("Please verify your PIN first.")
            return
        amount = float(input("Enter the amount you want to deposit: $"))
        if amount > 0:
            self.bankAccount.balance += amount
            print("You have deposited $", amount, "successfully.")
        else:
            print("Invalid deposit.")

    def withdraw(self):
        if not self.authenticated:
            print("Please verify your PIN first.")
            return
        amount = float(input("Enter the amount you want to withdraw: $"))
        if amount > 0:
            if amount <= self.bankAccount.balance:
                self.bankAccount.balance -= amount
                print("You have withdrawn $", amount, "successfully.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal.")

    def checkBalance(self):
        if not self.authenticated:
            print("Please verify your PIN first.")
            return
        print("Your current balance is $", self.bankAccount.balance)


class bankAccount:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance


user1 = bankAccount("Kevin", 1234, 1000)
user1ATM = ATM()

user1ATM.insertCard(user1)

user1ATM.deposit()
user1ATM.checkBalance()
user1ATM.withdraw()
user1ATM.checkBalance()
