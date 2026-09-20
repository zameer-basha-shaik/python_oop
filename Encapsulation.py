# Encapsulation

class BankAccount:

    def __init__(self, amount = 0.0):
        self._balance = amount

    @property
    def balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient Funds")
            return
        self._balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount has to be Positive!")
        self._balance += amount



acc1 = BankAccount(100.0)
acc2 = BankAccount()

acc1.withdraw(50)
acc2.deposit(200)

print(acc1.balance)
print(acc2.balance)