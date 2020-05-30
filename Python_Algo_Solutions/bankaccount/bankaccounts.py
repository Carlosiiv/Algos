class BankAccount:
    
    def __init__(self,balance=0,interest=.01):
        self.balance = balance
        self.interest = interest
    def deposit(self,amount):
        self.balance += amount
        print(f'Deposit of ${amount} Successful')
        return self
    
    def withdraw(self,amount):
        if self.balance < amount:
            self.balance - amount - 5
            print(f'Withdraw of ${amount} Successful, Be aware we are changing a $5 dollar fee  ')
            return self
        else:
            print(f'Withdraw of ${amount} Successful')
        return self
    
    def display_account_info(self):
        if self.balance > 0 :
            interest = (self.interest * self.balance) + self.balance
            interest_earned = (self.interest * self.balance)
            print(f'Your current balance {self.balance} & Your current interest earned is ${interest_earned}')
            return self
        else:
            print(f'Your current balance is ${self.balance}')
            return self
        
    def yield_interest(self):
        if self.balance > 0:
            interest = (self.interest * self.balance)
            self.balance += interest
            print(f'Your Current balance plus interest is {self.balance}')
        else:
            print(f'You owe me money!')
        return self
    
    def display_balance(self):
        print(self.balance)
        return self
        
    def make_transfer(self,receiver,transfer_amount=0):
        b = self.account.balance
        b -= transfer_amount
        self.account.balance = b
        you = self.first_name
        receiver.balance += transfer_amount
        print(f'{you} Transfer  is Completed! Your Current Balance is {b}')
        return self
    
account_01 = BankAccount(500.00)
account_02 = BankAccount(50.00)
account_03 = BankAccount(-22.00)

# account_01.deposit(15).deposit(12).deposit(44).withdraw(45).yield_interest()
# account_02.deposit(13).deposit(55).withdraw(22).withdraw(11).withdraw(1).withdraw(12).display_account_info()
#account_03.display_account_info().withdraw(70).yield_interest().deposit(10).display_account_info()
