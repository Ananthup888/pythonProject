#class account       self.balance =0
#def deposit()     balance+amount
#def withdraw      balance>amount    balance=balance-amount
#                  balance<amount     'insufficient balance'
#def enquiry()     balance

class Account:
    def __init__(self):
        self.balance=0
    def deposit(self):
        amount=int(input("enter the amount to deposit"))
        self.balance=amount+self.balance
    def withdraw(self):
        amount = int(input("enter the amount to withdraw"))
        if(amount>self.balance):
            print("Insufficient balance")
        else:
            self.balance=self.balance-amount
    def enquiry(self):
        print("Your balance is",self.balance)
ac1=Account()
ac1.deposit()
ac1.withdraw()
ac1.enquiry()
