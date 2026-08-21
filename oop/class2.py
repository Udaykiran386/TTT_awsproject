class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private
        print("Account is created "+owner+" "+str(balance))

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
            return
        self.__balance -= amount
        print(f"Withdrew ₹{amount}. New balance: ₹{self.__balance}")

    def get_balance(self):
        return self.__balance


account = BankAccount("sreenu", 100000)
account.deposit(2000)          # Deposited ₹2000. New balance: ₹7000
account.withdraw(1000)         # Withdrew ₹1000. New balance: ₹6000

# print(account.__balance)     # ❌ AttributeError
print(account.get_balance())   # ✅ 6000

# # Name mangling in action - Python doesn't make this IMPOSSIBLE, just inconvenient:
print(account._BankAccount__balance)   # 6000 - technically still reachable, but nobody should do this