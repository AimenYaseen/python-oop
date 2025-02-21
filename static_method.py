"""
Private and Protected are defined the same way we defined private and protected attributes
"""

class BankAccount:
    MIN_BALANCE = 500

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    # protected method
    def _is_valid_amount(self, amount):
        return amount > 0
    
    # private method
    def __log_transaction(self, transaction_type, amount):
        print(f"{transaction_type} transaction: {amount}. Now balance is {self._balance}")

    def deposit_balance(self, amount):
        if not self._is_valid_amount(amount):
            print("Amount must be greater than 0")
        self._balance += amount
        self.__log_transaction("Deposit", amount)
    
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 < rate < 1
    
account = BankAccount("John", 1000)
account.deposit_balance(500)
