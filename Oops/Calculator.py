class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
        
    def debit(self, amount):
        self.balance -= amount
        print(amount,"is debited from acoount so final balance is", self.balance)
    
    def credit(self, amount):
        self.balance += amount
        print(amount,"is credited in account so final balance is", self.balance)
    
acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)