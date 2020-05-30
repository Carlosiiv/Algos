import bankaccounts

class User:
    
# Attributes of the Users // requirements

    def __init__(self,first_name='none',last_name='none'):
        self.first_name = first_name
        self.last_name = last_name
        self.account = {
            'checking': bankaccounts.BankAccount(balance=0, interest=.01),
            'savings': bankaccounts.BankAccount(balance=0, interest=.01)
            }
        
# Methods of the Users // What they can do

    # withdrawl
    
    # def make_withdrawl(self, withdrawl_amount = 0):
    #     self.account.display_balance -= self.account.withdraw
        
    #     print(f"${withdrawl_amount} Withdrawl Successful")
    #     return self
    
    # #current balance
    
    # def display_balance(self):
    #     self.account.display_balance()
    #     you = self.first_name
    #     print(f'{you} your current balance is ${self.account.display_balance}')
    #     return self  
    
    # #deposit
    
    # def make_deposit(self, deposit_amount = 0):
    #     b = self.account.balance
    #     b += deposit_amount
    #     self.account.balance = b
    #     print(f'${deposit_amount} Deposit Successful')
    #     return self
    
    # #user Transfer
    
    # def make_transfer(self,receiver,transfer_amount=0):
    #     b = self.account.balance
    #     b -= transfer_amount
    #     self.account.balance = b
    #     you = self.first_name
    #     receiver.balance += transfer_amount
    #     print(f'{you} Transfer  is Completed! Your Current Balance is {b}')
    #     return self
    
Carlos = User('Carlos','Michel')
Rowan = User('Rowan', 'Not Sure') 
Derrick = User('Derrick', 'N')

# Carlos.display_balance()
Carlos.account['checking'].deposit(50).display_account_info().display_balance()