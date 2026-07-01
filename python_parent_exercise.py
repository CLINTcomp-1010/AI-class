class BankAccount:
    def __init__(self, balance=0):
        self._balance = 0
        self.set_balance(balance)

    def set_balance(self, amount):
        if amount < 0:
            print("insufficiient fund!")
        else:
            self._balance = amount

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 10:
            print("Deposit 10-9999999999 dollars!")
        else:
            self._balance += amount
            print(f"Deposited: {amount}. New balance: {self._balance}")

    def withdraw(self, amount):
        fee = 0

        if amount > 2000:
            fee = 20

        total_deduction = amount + fee

        if total_deduction > self._balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("withdraw invalid!!, Withdraw 0ver 0 dollar.")
        else:
            self._balance -= total_deduction
            print(f"Withdrawn: {amount}, Fee: {fee}. New balance: {self._balance}")

acct = BankAccount(5000)

# Will include ₦20 fee
print(acct.deposit(5000),
      acct.withdraw(2000),
      acct.withdraw(1000),
      acct.get_balance())