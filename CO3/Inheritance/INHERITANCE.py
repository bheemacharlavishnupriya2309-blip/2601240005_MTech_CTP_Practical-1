class BankAccount:
    def __init__(self, holder_name, account_number, balance):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print("Account Holder:", self.holder_name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance + 5000:
            self.balance -= amount
            print("Withdrawal Successful")
        else:
            print("Withdrawal Limit Exceeded")


name = input("Enter Account Holder Name: ")
number = input("Enter Account Number: ")
balance = float(input("Enter Initial Balance: "))

account_type = input("Enter Account Type (Savings/Current): ")
amount = float(input("Enter Withdrawal Amount: "))

if account_type.lower() == "savings":
    account = SavingsAccount(name, number, balance)
elif account_type.lower() == "current":
    account = CurrentAccount(name, number, balance)
else:
    print("Invalid Account Type")
    exit()

account.withdraw(amount)
account.display()