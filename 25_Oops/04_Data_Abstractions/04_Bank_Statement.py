from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def interest_rate(self):
        pass

class SavingsAccount(Bank):
    def interest_rate(self):
        return "Savings Account: 5% interest"

class CurrentAccount(Bank):
    def interest_rate(self):
        return "Current Account: 3% interest"

# Usage
s = SavingsAccount()
c = CurrentAccount()

print(s.interest_rate())
print(c.interest_rate())
