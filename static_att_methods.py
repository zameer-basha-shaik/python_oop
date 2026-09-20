# Static Attributes and Methods
# Protected and Private Methods

class BankAccount:
    num_accs = 0 # Static Attributes
    def __init__(self, owner, amount = 0):
        self.owner = owner
        self._balance = amount
        BankAccount.num_accs += 1

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance+=amount
            self.__log_transaction('Deposit', amount)
        else:
            print("Amount Should be greater than 0")

    def _is_valid_amount(self, amount): # Protected Methods
        return amount > 0

    def __log_transaction(self, transaction_type, amount): # Private method
        print(f"Logging {transaction_type} of ${amount}, New Balance: {self._balance}")

    @staticmethod # Static Method
    def is_valid_rate(rate):
        return 0 <= rate <=5

acc1 = BankAccount('John', 200)
acc2 = BankAccount('Bob', 300)

# acc1.__log_transaction("Deposit", 400) "Throws error since private"

print(f"Number of Accounts: {BankAccount.num_accs}")
print(f"Is interest rate 5 valid?: {BankAccount.is_valid_rate(5)}")

acc1.deposit(100)