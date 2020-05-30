class User:
# Attributes of the Users // requirements
    def __init__(self,first_name='none',last_name='none',balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
# Methods of the Users // What they can do
    # withdrawl
    def make_withdrawl(self, withdrawl_amount = 0):
        b = self.balance 
        b -= withdrawl_amount
        self.balance = b
        print(f"${withdrawl_amount} Withdrawl Successful")
        return self
    #current balance
    def display_balance(self):
        b = self.balance
        you = self.first_name
        print(f'{you} your current balance is ${b}')
        return self  
    #deposit
    def make_deposit(self, deposit_amount = 0):
        b = self.balance
        b += deposit_amount
        self.balance = b
        print(f'${deposit_amount} Deposit Successful')
        return self
    #user Transfer
    def make_transfer(self,receiver,transfer_amount=0):
        b = self.balance
        b -= transfer_amount
        self.balance = b
        you = self.first_name
        receiver.balance += transfer_amount
        print(f'{you} Transfer  is Completed! Your Current Balance is {b}')
        return self
Carlos = User('Carlos','Michel',100)
Rowan = User('Rowan', 'Not Sure',500) 
Derrick = User('Derrick', 'Not Sure',600)

# Carlos.display_balance()
Derrick.make_transfer(Carlos,50)
Carlos.display_balance()
Carlos.make_withdrawl(25).display_balance().make_deposit(500).make_deposit(50).display_balance() 