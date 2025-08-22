class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid withdrawal!")

# Usage
acc = BankAccount(1000)
print(acc.get_balance())  # ✅ Access through method
acc.deposit(500)
print(acc.get_balance())
acc.withdraw(200)
print(acc.get_balance())
