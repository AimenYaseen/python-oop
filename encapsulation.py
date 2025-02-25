"""
Encapsulate the internal working and only expose the necessary parts to the outside world.
Encapsulation is achieved by using private attributes and methods.
Private attributes and methods are defined by prefixing the attribute or method name with two underscores.

User don't have to worry about the internal working of the class.
User only needs to know how to interact with the class.
Encapsulation helps to hide the internal working of a class from the user.
Encapsulation helps to prevent the user from accidentally modifying the internal state of the class.
"""

class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance

bank = BadBankAccount(1000)
bank.balance = -1
print(bank.balance)
# NOT GOOD

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance is {self._balance}")
        else:
            print("Amount must be greater than 0")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance is {self._balance}")
        else:
            print("Invalid amount")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.balance)
account.balance = -1   # AttributeError: can't set attribute
print(account.balance)