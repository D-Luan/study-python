class BankAccount:
    def __init__(self, account_holder: str):
        self.account_holder = account_holder 
        self._balance = 0.0       

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Invalid balance: Balance cannot be negative.")
        self._balance = value

c = BankAccount("Annie")
c.balance = 100.0
print(f"Account holder: {c.account_holder}, Balance: {c.balance}") 

try:
    c.balance = -2
except ValueError as e:
    print(e)