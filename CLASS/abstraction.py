#Abstraction - data hiding
class Account:
    def __init__(self):
        self.balance=0
    def deposit(self):
        amount=int(input("enter the amount to deposit"))
        self.__balance=amount+self.balance   #strongly private
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