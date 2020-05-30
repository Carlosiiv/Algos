from bankaccounts import BankAccount

class User:
# Attributes of the Users // requirements
    def __init__(self,first_name='none',last_name='none'):
        self.first_name = first_name
        self.last_name = last_name
        self.account = BankAccount(balance = 0, interest = .01 )
# Methods of the Users // What they can do
    # withdrawl
    def make_withdrawl(self, withdrawl_amount = 0):
        b = self.account.balance
        b -= withdrawl_amount
        self.account.balance = b
        print(f"${withdrawl_amount} Withdrawl Successful")
        return self
    #current balance
    def display_balance(self):
        b = self.account.balance
        you = self.first_name
        print(f'{you} your current balance is ${b}')
        return self  
    #deposit
    def make_deposit(self, deposit_amount = 0):
        b = self.account.balance
        b += deposit_amount
        self.account.balance = b
        print(f'${deposit_amount} Deposit Successful')
        return self
    #user Transfer
    def make_transfer(self,receiver,transfer_amount=0):
        b = self.account.balance
        b -= transfer_amount
        self.account.balance = b
        you = self.first_name
        receiver.account.balance += transfer_amount
        print(f'{you} Transfer  is Completed! Your Current Balance is {b}')
        return self
Carlos = User('Carlos','Michel',100)
Rowan = User('Rowan', 'Not Sure',500) 
Derrick = User('Derrick', 'Not Sure',600)

# Carlos.display_balance()
Derrick.make_transfer(Carlos,50)
Carlos.display_balance()
Carlos.make_withdrawl(25).display_balance().make_deposit(500).make_deposit(50).display_balance() 