1.
class Account:
    def __init__(self, name):
        self.name = name
        self.balance=0

account = Account(name="Rigel")
assert account.name == "Rigel"

2.
class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    def deposit(self, quantity):
            self.balance += quantity

account=Account(name="Rigel")
assert account.name == "Rigel"

assert account.balance==0
account.deposit(500)
assert account.balance==500

3.
class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    def deposit(self, quantity):
            self.balance += quantity
    def withdraw(self, quantity):
        if quantity>self.balance:
            raise InsufficientFundsError("InsufficientFundsError")
        self.balance -= quantity

account=Account(name="Rigel")
assert account.name == "Rigel"

assert account.balance==0
account.deposit(500)
assert account.balance==500

account.withdraw(200)
assert account.balance==300

try:
    account.withdraw(400)
except InsufficientFundsError:
    print("Insufficient Funds Error")



