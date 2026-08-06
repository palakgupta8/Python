class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawal:", amount)

    def check_balance(self):
        print("Current balance:", self.__balance)


bank = BankAccount(50000)

bank.deposit(500)
bank.check_balance()

bank.withdraw(90000)
bank.check_balance()