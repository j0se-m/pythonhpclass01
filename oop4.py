class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"

# Create a subclass of BankAccount for a Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.01):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Added interest: ${interest}")

# Create a SavingsAccount
savings_account = SavingsAccount("Jane Smith", 1000, 0.02)

# Deposit, withdraw, and add interest
savings_account.deposit(500)
savings_account.withdraw(200)
savings_account.add_interest()

# Print account details
print(savings_account)
