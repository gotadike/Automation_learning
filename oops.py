class Account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0

    def check_balance(self):
        print(f"balance --{self._balance}")

    def deposit(self, amount):
        self._balance += amount
        print(f"deposit done --{self._balance}")

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"withdraw of --{amount} done and balance--{self._balance}")
        else:
            print("low balance")


class SavingsAccount(Account):
    def calculate_interest(self):
        INTEREST_RATE = 0.04
        interest = self._balance * INTEREST_RATE
        print(f"interest added --- {interest}")

class CurrentAccount(Account):
    def withdraw(self, amount):
        OVERDRAFT_LIMIT = 1000
        if self._balance + OVERDRAFT_LIMIT >= amount:
            self._balance -= amount
            print(f"withdraw of --{amount} done and balance--{self._balance}")
        else:
            print("limit exceeded")

class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.__accounts = {}

    def create_account(self, id, holder_name, type):
        if type=="savings":
            new_account = SavingsAccount(id, holder_name)
        elif type=="current":
            new_account = CurrentAccount(id, holder_name)
        self.__accounts[id] = new_account
        print("account created")
        return new_account

    def get_account(self, id):
        if id not in self.__accounts:
            print("id not found")
        else:
            account = self.__accounts[id]
            print(f"\n ID : {account.id}\n holder name: {account.holder_name}")
            return account


sbk = Bank("bank of rr", "bengaluru")
sbk.create_account("1", "sid", "savings")

s1 = sbk.create_account("1", "sid", "savings")
c1 = sbk.create_account("1", "sid", "current")

s1.deposit(1000)
c1.deposit(30)

s1.withdraw(2000)
c1.withdraw(40)
