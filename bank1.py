class account:
    def __init__(self,name,account_number,balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        (f"{self.name} Deposited {amount} $.Current balance is:{self.balance}")

    def withdraw(self,amount):
        
        if self.balance >= amount:
            self.balance -= amount
            (f"{self.name} withdraw {amount} $.Current balance is: {self.balance}")
        
        else:
            ("you don't have enough  funds to withdraw.")

            ("not working")

class Savings_Account(account):
    def __init__(self,name,account_number,balance,interest_rate):
        super().__init__(name,account_number,balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self.balance)*(self.interest_rate)
        self.deposit(interest)
account1 = account("alex", "123745",1000)
account1.deposit(500)
account1.withdraw(200)

Saving_Account = Savings_Account("alex","968765", 2000,0.01)
Saving_Account.deposit(1000)
Saving_Account.add_interest()
Saving_Account.withdraw(500)
Saving_Account.deposit(99937)